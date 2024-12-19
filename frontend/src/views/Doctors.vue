<template>
    <p class="mx-32  text-[16px] text-gray-600 font-medium ">Browse through the doctors specialist.</p>

    <div class="flex flex-col md:flex-row gap-4 p-6  mx-20 h-auto">

        <div class="flex flex-col gap-3 px-4 w-64">
            <button v-for="specialist in specialists" :key="specialist" @click="fetchDoctors(specialist)"
                :class="['w-full pr-10 py-2 border border-gray-300  rounded-sm text-gray-600 shadow-sm',
                    activeSpecialist === specialist ? 'bg-indigo-200 border border-black text-white font-semibold text-sm' : 'bg-white hover:bg-gray-100  text-sm text-gray-600 font-medium ']">
                {{ specialist }}
            </button>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-6 w-full pt-10">
            <All_doctors />
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import All_doctors from "./All_doctors.vue";
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