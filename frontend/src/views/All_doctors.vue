<template>
    <div class="bg-white mx-4 md:mx-16 lg:mx-40">
        <main class="container mx-auto px-4 py-8">
            <div class="flex flex-col gap-8 justify-center sm:flex-row sm:gap-4 md:gap-6 lg:gap-8 mb-6">
                <!-- Filter Section -->
                <div class="w-full sm:w-3/4 lg:w-2/3">
                    <div class="flex flex-wrap gap-2 p-2">
                        <!-- Filter Button -->
                        <button
                            class="flex items-center space-x-2 px-4 py-2 text-[#224855] border border-[#224855] rounded-md">
                            <i class="fa fa-filter text-[#224855]" aria-hidden="true"></i>
                            <span>Filter</span>
                        </button>

                        <!-- Dropdowns -->
                        <select v-model="activeSpecialist" @change="fetchDoctors"
                            class="px-4 py-2 rounded-md text-sm border border-[#224855] text-[#224855] bg-transparent outline-none">
                            <option value="">Speciality</option>
                            <option v-for="specialist in specialists" :key="specialist.name1" :value="specialist.name1">
                                {{ specialist.name1 }}
                            </option>
                        </select>

                        <select
                            v-if="doctors.length > 0"
                            v-model="selectedGender"
                            @change="fetchDoctors"
                            class="px-4 py-2 rounded-md text-sm border border-[#224855] text-[#224855] bg-transparent outline-none">
                            <option value="">Gender</option>
                            <!-- Loop through unique genders -->
                            <option v-for="gender in uniqueGenders" :key="gender" :value="gender">{{ gender }}</option>
                        </select>

                        <select
                            class="px-4 py-2 rounded-md text-sm border border-[#224855] text-[#224855] bg-transparent outline-none">
                            <option>Language</option>
                        </select>
                        <select
                            class="px-4 py-2 rounded-md text-sm border border-[#224855] text-[#224855] bg-transparent outline-none">
                            <option>Sort</option>
                        </select>
                    </div>

                    <h2 v-if="doctors.length > 0" class="text-md font-bold text-[#224855] py-4">
                        Search Result ({{ doctors.length }})
                    </h2>

                    <div v-for="doctor in doctors" :key="doctor.full_name">
                        <div class="bg-white rounded-lg shadow-md px-4 py-8 mb-4 flex flex-col sm:flex-row items-center border border-gray-200">
                            <img :src="doctor.doctor_image" :alt="doctor.full_name[0]" alt="Doctor"
                                class="h-20 w-20 rounded-full border-2 border-gray-300">
                            <div class="mt-4 sm:mt-0 sm:ml-4 px-2 text-center sm:text-left">
                                <h3 class="text-md font-bold text-[#224855]">{{ doctor.full_name }}</h3>
                                <p class="text-[12px] font-normal text-[#367892] border-b py-2">
                                    {{ doctor.specialist }} | {{ doctor.experience }}
                                </p>
                                <p class="text-sm text-gray-500 py-2 flex gap-1 justify-center sm:justify-start">
                                    <img class="w-4 h-4" src="../assets/icons8-location.gif" alt="">
                                    {{ doctor.address }}
                                </p>
                                <p class="text-sm flex gap-2 text-gray-500 justify-center sm:justify-start">
                                    <img src="https://www.askapollo.com/assets/images/language.svg" alt="">
                                    {{ doctor.language }}
                                </p>
                                <p class="text-sm flex gap-2 text-gray-500 justify-center sm:justify-start">
                                    <img src="https://www.askapollo.com/assets/images/qualification.svg" alt="">
                                    {{ doctor.qulifications }}
                                </p>
                            </div>
                            <div v-if="doctor.shifts && doctor.shifts.length > 0"
                                class="mt-4 sm:mt-0 sm:ml-auto text-right">
                                <p class="text-sm font-semibold text-green-600">MON - SAT</p>
                                <div v-for="shift in doctor.shifts" :key="shift.name">
                                    <p class="text-sm text-[#03a9d9]">
                                        ( {{ formatTime(shift.start_time) }} - {{ formatTime(shift.end_time) }})
                                    </p>
                                </div>
                                <button class="bg-[#005488] text-white px-4 text-[10px] py-2 rounded-md mt-4"
                                    @click="goToDoctorDetails(doctor.full_name, doctor.specialist)">
                                    BOOK APPOINTMENT
                                </button>
                            </div>
                            <div v-else class="mt-4 sm:mt-0 sm:ml-auto text-right">
                                <button
                                    class="bg-[#30627e] opacity-50 cursor-not-allowed text-white px-4 text-[10px] py-2 rounded-md mt-4">
                                    BOOK APPOINTMENT
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Image Section -->
                <div class="w-full sm:w-1/4 lg:w-1/3 h-auto relative">
                    <div class="sticky border rounded-lg p-10 top-24">
                        <img class="w-full h-full object-cover" src="../assets/need-help.svg" alt="Need Help">
                    </div>
                    <div class="absolute top-32 text-center font-bold left-1/2 transform -translate-x-1/2 pl-8">
                        <p class="text-[#F4A100] text-sm">Need Help?</p>
                        <p class="hover:text-[#F4A100]">1860 500 1066</p>
                    </div>
                </div>
            </div>
        </main>
    </div>
</template>
<script setup>
import axios from "axios";
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const doctors = ref([]);
const allDoctors = ref([]);
const specialists = ref([]);
const activeSpecialist = ref("");
const selectedGender = ref("");

// Fetch doctors data
const fetchDoctorsData = async () => {
    try {
        const response = await axios.get(
            "api/method/appointments_management.controllers.api.doctors_data"
        );
        doctors.value = response.data.message || [];
        allDoctors.value = doctors.value;
    } catch (error) {
        console.error("Error fetching doctors data:", error);
    }
};

// Fetch specialists data
const fetchSpecialists = async () => {
    try {
        const response = await axios.get(
            "api/method/appointments_management.controllers.api.spaclist"
        );
        specialists.value = response.data.message || [];
    } catch (error) {
        console.error("Error fetching specialists data:", error);
    }
};

// Filter doctors based on specialist and gender
const fetchDoctors = () => {
    doctors.value = allDoctors.value.filter((doctor) => {
        const matchesSpecialist = activeSpecialist.value
            ? doctor.specialist === activeSpecialist.value
            : true;

        const matchesGender = selectedGender.value
            ? doctor.gender === selectedGender.value
            : true; // Apply gender filter only if selectedGender is not empty

        return matchesSpecialist && matchesGender;
    });
};

// Extract unique genders from doctors
const uniqueGenders = computed(() => {
  const genders = allDoctors.value.map(doctor => doctor.gender).filter(Boolean);
  return [...new Set(genders)]; // Remove duplicates using Set
});

// Format time for shifts
const formatTime = (time) => {
    const [hour, minute] = time.split(":").map(Number);
    const period = hour >= 12 ? "PM" : "AM";
    const formattedHour = hour % 12 || 12;
    return `${formattedHour}:${minute.toString().padStart(2, "0")} ${period}`;
};

// Navigate to doctor's details page
const goToDoctorDetails = (full_name, specialist) => {
    router.push({ name: "Doctor_details", params: { full_name, specialist } });
};

// Fetch data on mount
onMounted(() => {
    fetchDoctorsData();
    fetchSpecialists();
});
</script>
