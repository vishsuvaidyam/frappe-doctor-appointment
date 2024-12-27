<template>
    <div class="w-full inset-0 px-20 pt-10 " v-for=" doctor in doctorDetails">
        <div class="flex gap-10 w-full h-auto">
            <div class="w-1/6  ">
                <div class="border rounded-lg bg-blue-600">
                    <img class="h-64 flex justify-center" :src="doctor.doctor_image" />
                </div>
            </div>
            <div class="w-4/5 border border-gray-300 rounded-lg">

                <div class=" px-8 py-8 ">
                    <h1 class="text-3xl text-gray-700 font-bold py-1 flex items-center gap-2">
                        {{ doctor.name }}
                        <img class="w-4 h-4" src="../assets/download (1).svg" alt="" srcset="">
                    </h1>
                    <p class="text-md text-gray-700 font-normal py-1">{{ doctor.qulifications }}-{{ doctor.specialist }}
                        <span class="border px-4 py-1  rounded-3xl">{{ doctor.experience }}</span>
                    </p>
                    <p class="flex gap-2 items-center text-md font-semibold py-2">About
                        <span class="">
                            <img src="../assets/download.svg" alt="" srcset="">
                        </span>
                    </p>
                    <div class="w-3/5">
                        <p class="text-sm font-normal text-gray-600 "> {{ doctor.description }}

                        </p>
                    </div>
                    <p class="text-md font-semibold pt-4 text-gray-500">Apointment fee:<span
                            class="text-md font-semibold px-2 text-gray-800">${{ doctor.doctor_fee }}</span></p>
                </div>
            </div>
        </div>

        <div class="flex gap-10 w-full h-64 pt-8">
            <div class="w-1/6  ">
            </div>
            <div class="w-4/5">
                <h1>Booking slots</h1>
                <div class="pt-4 flex gap-4">
                    <button class="px-2 text-sm font-normal py-10 border rounded-full">THU 12</button>
                    <button class="px-2 text-sm font-normal py-10 border rounded-full">THU 12</button>
                    <button class="px-2 text-sm font-normal py-10 border rounded-full">THU 12</button>
                    <button class="px-2 text-sm font-normal py-10 border rounded-full">THU 12</button>
                    <button class="px-2 text-sm font-normal py-10 border rounded-full">THU 12</button>
                    <button class="px-2 text-sm font-normal py-10 border rounded-full">THU 12</button>
                    <button class="px-2 text-sm font-normal py-10 border rounded-full">THU 12</button>
                </div>
                <div class="flex gap-4 pt-4">
                    <button class="px-8 py-2 border rounded-full">10:30 am</button>
                    <button class="px-8 py-2 border rounded-full">10:30 am</button>
                    <button class="px-8 py-2 border rounded-full">10:30 am</button>
                    <button class="px-8 py-2 border rounded-full">10:30 am</button>
                    <button class="px-8 py-2 border rounded-full">10:30 am</button>
                    <button class="px-8 py-2 border rounded-full">10:30 am</button>
                </div>
                <button class="px-10 py-3 border rounded-3xl mt-4 bg-blue-600 text-white text-sm font-normal">Book an
                    appointment</button>
            </div>
        </div>

        <div class="pt-20">
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
                        <span :class="doctor.status === 'Available' ? 'text-green-500' : 'text-red-500'"
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
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const router = useRouter()
const route = useRoute();
const allDoctors = ref([]);
const doctorDetails = ref([]);

const fetchDoctors = async () => {
    try {
        console.log("Route Param Full Name:", route.params.full_name);
        console.log("Route Param Specialist:", route.params.specialist);

        // Fetch all filter doctors
        const doctorsResponse = await axios.get(
            "/api/method/appointments_management.controllers.api.doctors_filter"
        );

        if (doctorsResponse.data.message) {
            allDoctors.value = doctorsResponse.data.message.filter(
                (doctor) => doctor.specialist === route.params.specialist
            );
            console.log(allDoctors.value, '=================');
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

onMounted(fetchDoctors)
</script>
