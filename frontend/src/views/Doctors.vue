<template>
    <p class="mx-32 text-[16px] text-gray-600 font-medium pt-10">
        Browse through the doctor's specialties.
    </p>
    <div class="flex flex-col md:flex-row gap-4 p-6 mx-20 h-auto">
        <div class="flex flex-col gap-3 px-4 w-64">
            <button v-for="specialist in specialists" :key="specialist.id" @click="fetchDoctors(specialist)" :class="[
                'w-full pr-10 py-2 border border-gray-300 rounded-sm shadow-sm text-sm font-medium',
                activeSpecialist === specialist
                    ? 'bg-indigo-200 border-black text-white font-semibold'
                    : 'bg-white hover:bg-gray-100 text-gray-600',
            ]">
                {{ specialist.name1 }}
            </button>
            <button @click="fetchDoctors(null)" :class="[
                'w-full py-2 border rounded-sm shadow-sm text-sm font-medium',
                !activeSpecialist
                    ? 'bg-indigo-200  text-white font-semibold'
                    : 'bg-white hover:bg-gray-100 text-gray-600',
            ]">
                Show All
            </button>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 w-full">
            <div v-for="doctor in doctors" :key="doctor.full_name" @click="goToDoctorDetails(doctor.full_name)"
                class="bg-white shadow-md rounded-xl border border-indigo-200 text-start cursor-pointer transition ease-in-out delay-150 hover:-translate-y-4   duration-300">
                <div class="bg-[#e1e5ff] p-6 rounded-t-xl">
                    <img class="w-full h-54 " :src="doctor.doctor_image" :alt="doctor.full_name[0]" />
                </div>
                <div class="  p-6">
                    <span :class="doctor.status === 'Available' ? 'text-green-500' : 'text-red-500'"
                        class="text-sm font-medium">
                        ● {{ doctor.status }}
                    </span>
                    <h3 class="text-lg font-semibold text-gray-800 mt-2">
                        {{ doctor.full_name }}
                    </h3>
                    <p class="text-sm text-gray-600">{{ doctor.specialist }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();
const specialists = ref([]);
const doctors = ref([]);
const allDoctors = ref([]);
const activeSpecialist = ref(null);

const fetchData = async () => {
    try {
        const [specialistsResponse, doctorsResponse] = await Promise.all([
            axios.get("api/method/appointments_management.controllers.api.spaclist"),
            axios.get("api/method/appointments_management.controllers.api.doctors_filter"),
        ]);
        specialists.value = specialistsResponse.data.message || [];
        allDoctors.value = doctorsResponse.data.message || [];
        doctors.value = allDoctors.value;
    } catch (error) {
        console.error("Error fetching data:", error);
    }
};

const fetchDoctors = (specialist) => {
    activeSpecialist.value = specialist;
    doctors.value = specialist
        ? allDoctors.value.filter((doc) => doc.specialist === specialist.name1)
        : allDoctors.value;
};

const goToDoctorDetails = (full_name) => {
    router.push({ name: "Doctor_details", params: { full_name } });
};

onMounted(fetchData);
</script>

<style>
button {
    transition: background-color 0.2s, color 0.2s;
}
</style>