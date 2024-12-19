<template>
    <p class="mx-32  text-[16px] text-gray-600 font-medium ">Browse through the doctors specialist.</p>

    <div class="flex flex-col md:flex-row gap-4 p-6  mx-20 h-auto">
        <!-- siderbar Buttons -->
        <div class="flex flex-col gap-3 px-4 w-64">
            <button v-for="specialist in specialists" :key="specialist" @click="fetchDoctors(specialist)" 
                    :class="['w-full pr-10 py-2 border border-gray-300  rounded-sm text-gray-600 shadow-sm',
                    activeSpecialist === specialist ? 'bg-indigo-200 border border-black text-white font-semibold text-sm' : 'bg-white hover:bg-gray-100  text-sm text-gray-600 font-medium ']">
                    {{ specialist }}
            </button>
        </div>
        <!-- Doctor Cards -->
        <!-- <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6 w-full ">
            <div v-for="(doctor, index) in doctors" :key="index"
                class="bg-white shadow-md rounded-lg border-t-4 border-blue-500 p-6 hover:transition-transform duration-300  ">
                <div>
                    <img class="w-full h-54 mx-auto" :src="doctor.doctor_image" :alt="`${doctor.full_name[0]}`" />
                </div>
                <div class="mt-4">
                    <span :class="{
                        'text-green-500': doctor.status === 'Available',
                        'text-red-500': doctor.status !== 'Available',
                    }" class="text-sm font-medium">
                        ● {{ doctor.status }}
                    </span>
                    <h3 class="text-lg font-semibold text-gray-800 mt-2">{{ doctor.full_name }}</h3>
                    <p class="text-sm text-gray-600">{{ doctor.specialist }}</p>
                </div>
            </div>
        </div> -->
        <!-- <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6 pt-5 w-full">
    <div v-for="(doctor, index) in doctors" :key="index"
        class="bg-white shadow-md rounded-lg border-t-4 border-blue-500 p-6 transform transition-transform cursor-pointer hover:shadow-lg hover:translate-y-[-10px]">
        <div>
            <img class="w-full h-54 mx-auto" :src="doctor.doctor_image" :alt="`${doctor.full_name[0]}`" />
        </div>
        <div class="mt-4">
            <span :class="{
                'text-green-500': doctor.status === 'Available',
                'text-red-500': doctor.status !== 'Available',
            }" class="text-sm font-medium">
                ● {{ doctor.status }}
            </span>
            <h3 class="text-lg font-semibold text-gray-800 mt-2">{{ doctor.full_name }}</h3>
            <p class="text-sm text-gray-600">{{ doctor.specialist }}</p>
        </div>
    </div>
</div> -->

<div class=" px-2">
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6  w-full">
        <div v-for="(doctor, index) in doctors" 
            :key="index"
            class="bg-white shadow-md rounded-lg border-t-4 border-blue-500 p-6 transform transition-transform cursor-pointer hover:shadow-lg hover:translate-y-2 ">
            <!-- Doctor Image -->
            <div class="overflow-hidden rounded-md">
                <img 
                    class="w-full h-54 object-cover" 
                    :src="doctor.doctor_image" 
                    :alt="`${doctor.full_name[0]}`" 
                />
            </div>

            <!-- Doctor Details -->
            <div class="mt-4">
                <!-- Status Indicator -->
                <span 
                    :class="{
                        'text-green-500': doctor.status === 'Available',
                        'text-red-500': doctor.status !== 'Available',
                    }" 
                    class="text-sm font-medium">
                    ● {{ doctor.status }}
                </span>

                <!-- Name -->
                <h3 class="text-lg font-semibold text-gray-800 mt-2">
                    {{ doctor.full_name }}
                </h3>

                <!-- Specialist -->
                <p class="text-sm text-gray-600">
                    {{ doctor.specialist }}
                </p>
            </div>
        </div>
    </div>
</div>


    </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const specialists = ref([
    "General physician",
    "Gynecologist",
    "Dermatologist",
    "Pediatricians",
    "Neurologist",
    "Gastroenterologist",
]);
const activeSpecialist = ref(null);

const doctors = ref([]);
const fetchDoctors = async (specialist) => {
    activeSpecialist.value = specialist;
    try {
        const response = await axios.get("api/method/appointments_management.controllers.api.doctors_filter", {
            params: { specialist },
        });
        doctors.value = response.data.message || [];
    } catch (error) {
        console.error("Error fetching doctors:", error);
    }
};
fetchDoctors("");
</script>

<style>
button {
    transition: background-color 0.2s, color 0.2s;
}

</style>