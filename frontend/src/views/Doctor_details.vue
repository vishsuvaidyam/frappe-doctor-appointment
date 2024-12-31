<template>
    <div class="w-full inset-0 px-20 pt-10 " v-for=" doctor in doctorDetails">
        <div class="flex gap-10 w-full h-auto">
            <div class="w-1/6  ">
                <div class="border rounded-lg bg-blue-600">
                    <img class="h-64 flex justify-center" :src="doctor.doctor.doctor_image" />
                </div>
            </div>
            <div class="w-4/5 border border-gray-300 rounded-lg">

                <div class=" px-8 py-8 ">
                    <h1 class="text-3xl text-gray-700 font-bold py-1 flex items-center gap-2">
                        {{ doctor.doctor.full_name }}
                        <img class="w-4 h-4" src="../assets/download (1).svg" alt="" srcset="">
                    </h1>
                    <p class="text-md text-gray-700 font-normal py-1">{{ doctor.doctor.qulifications }}-{{
                        doctor.doctor.specialist }}
                        <span class="border px-4 py-1  rounded-3xl">{{ doctor.doctor.experience }}</span>
                    </p>
                    <p class="flex gap-2 items-center text-md font-semibold py-2">About
                        <span class="">
                            <img src="../assets/download.svg" alt="" srcset="">
                        </span>
                    </p>
                    <div class="w-3/5">
                        <p class="text-sm font-normal text-gray-600 "> {{ doctor.doctor.description }}

                        </p>
                    </div>
                    <p class="text-md font-semibold pt-4 text-gray-500">Apointment fee:<span
                            class="text-md font-semibold px-2 text-gray-800">${{ doctor.doctor.doctor_fee }}</span></p>
                </div>
            </div>
        </div>
       

        <div class="flex gap-10 w-full h-64 pt-8">
            <div class="w-1/6  ">
            </div>
            <div class="w-4/5">
                <h1>Booking Date</h1>
                <div class="flex items-center space-x-2">
                    <div class="relative pt-4">
                        <div class="flex gap-4 items-center">
                            <!-- Date Picker -->
                            <div class="relative">
                                <input type="date" id="date" v-model="selectedDate" :min="minDate" :max="maxDate"
                                    class="border border-gray-300 rounded-lg py-2 pl-10 pr-4 text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500" />
                                <span class="absolute left-2 top-2/4 transform -translate-y-2/4 text-gray-500">
                                    <CalendarIcon class="h-5 w-5 text-gray-500" />
                                </span>
                            </div>

                            <!-- Time Picker -->
                            <div class="relative">
                                <input type="time" id="time" v-model="selectedTime"
                                    class="border border-gray-300 rounded-lg py-2 pl-10 pr-4 text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500" />
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Book Appointment Button -->
                <div class="py-5">
                    <router-link to="/my-appointment"
                        @click="isFormValid ? bookAppointment(doctor.doctor.full_name, doctor.doctor.specialist, doctor.doctor.experience, doctor.doctor.doctor_image, doctor.doctor.address, doctor.doctor.doctor_fee ) : null"
                        :class="{
                            'px-10 py-3 border rounded-3xl text-white text-sm font-normal': true,
                            'bg-blue-600': isFormValid,
                            'bg-gray-300 cursor-not-allowed': !isFormValid
                        }" :disabled="!isFormValid">
                        Book an appointment
                    </router-link>
                </div>
            </div>
        </div>

        <div class="pt-10">
            <h1 class="text-center"> Related Doctors</h1>
            <p class="text-center">Simply browse through our extensive list of trusted doctors.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6 w-full py-10">
                <div v-for="related in allDoctors" :key="related.full_name"
                    @click="goToDoctorDetails(related.full_name, related.specialist)"
                    class="bg-white shadow-md h-50 rounded-xl border border-indigo-200 text-start cursor-pointer transition ease-in-out delay-150 hover:-translate-y-4   duration-300">
                    <div class="bg-[#e1e5ff]  p-4 rounded-t-xl">
                        <img class="w-full h-48 " :src="related.doctor_image" :alt="related.full_name[0]" />
                    </div>
                    <div class="  p-6">
                        <span :class="related.status === 'Available' ? 'text-green-500' : 'text-red-500'"
                            class="text-sm font-medium">
                            ● {{ related.status }}
                        </span>
                        <h3 class="text-lg font-semibold text-gray-800 mt-2">
                            {{ related.full_name }}
                        </h3>
                        <p class="text-sm text-gray-600">{{ related.specialist }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>
<script setup>
import axios from 'axios';
import { computed, onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { CalendarIcon } from '@heroicons/vue/solid';
import { useToast } from 'vue-toastification';
import { isLoggedIn } from '../auth';

const today = new Date();
const selectedDate = ref('');
const router = useRouter();
const route = useRoute();
const allDoctors = ref([]);
const doctorDetails = ref({});
const selectedTime = ref('');
const toast = useToast();

const isFormValid = computed(() => {
    return selectedDate.value && selectedTime.value;
});

const formattedDateTime = computed(() => {
    if (selectedDate.value && selectedTime.value) {
        const date = new Date(selectedDate.value);
        const options = { day: "2-digit", month: "long", year: "numeric" };
        const formattedDate = date.toLocaleDateString("en-US", options);
        const formattedTime = new Date(`1970-01-01T${selectedTime.value}`).toLocaleTimeString("en-US", {
            hour: "2-digit",
            minute: "2-digit",
        });
        return `${formattedDate} | ${formattedTime}`;
    }
    return '';
});

const fetchDoctors = async () => {
    try {
        console.log("Route Param Full Name:", route.params.full_name);
        console.log("Route Param Specialist:", route.params.specialist);

        // Fetch all filtered doctors
        const doctorsResponse = await axios.get(
            "/api/method/appointments_management.controllers.api.doctors_filter"
        );

        if (doctorsResponse.data.message) {
            allDoctors.value = doctorsResponse.data.message.filter(
                (doctor) => doctor.specialist === route.params.specialist
            );
            // console.log(allDoctors.value, '=================');
        } else {
            console.error("No doctors found.");
        }

        // Fetch doctor details
        const doctorDetailsResponse = await axios.get(
            "/api/method/appointments_management.controllers.api.doctor_details",
            {
                params: {
                    full_name: route.params.full_name,
                    specialist: route.params.specialist,
                },
            }
        );
        if (doctorDetailsResponse.data.message) {
            console.log(doctorDetailsResponse.data.message);

            doctorDetails.value = doctorDetailsResponse.data.message;
        } else {
            console.error("No data found for doctor.");
        }

    } catch (error) {
        console.error("Error fetching doctor details:", error);
    }
};

const goToDoctorDetails = (full_name, specialist) => {
    router.push({ name: "Doctor_details", params: { full_name, specialist } });
    fetchDoctors();
};


const bookAppointment = async (full_name, specialist, experience, doctor_image, address,doctor_fees,formatteddatetime) => {
    console.log(formattedDateTime,"=============================");
    
if (!isLoggedIn.value) { 
        toast.error("You need to log in to book an appointment.");
        router.push({ name: 'Login' });  
        return;
    }

    try {
        const response = await axios.post("/api/method/appointments_management.controllers.api.appointment_data", {
            doctor_name: full_name,
            patient: "John Doe",  
            specialist: specialist,
            experience: experience,
            doctor_image: doctor_image,
            address: address,
            doctor_fees:doctor_fees,doctor_fees,
            formattedDateTime: formattedDateTime.value,
        });
        if (response) {
            console.log(response.data.message);
            toast.success("Appointment booked successfully!");
        } else {
            console.log("Booking Response:", response.data);
        }
        
        router.push({
            name: "/my-appointment",
        });

    } catch (error) {
        console.error("Error booking appointment:", error);
    }
};



const currentYear = today.getFullYear();
const currentMonth = (today.getMonth() + 1).toString().padStart(2, '0');

const minDate = computed(() => {
    const day = today.getDate().toString().padStart(2, '0');
    return `${currentYear}-${currentMonth}-${day}`;
});

const maxDate = computed(() => {
    const lastDayOfMonth = new Date(currentYear, today.getMonth() + 2, 0).getDate();
    return `${currentYear}-${currentMonth}`;
});

onMounted(fetchDoctors);
</script>
