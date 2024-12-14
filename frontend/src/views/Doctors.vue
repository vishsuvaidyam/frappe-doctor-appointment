<template>
    <div class="flex flex-col md:flex-row gap-4 p-6 bg-gray-50 mx-20 h-auto">
        <!-- Sidebar (Categories) -->
        <div class="flex flex-col w-full md:w-1/4 space-y-4">
            <button
                class="px-4 py-2 bg-white border border-gray-300 rounded-lg text-gray-700 shadow-sm hover:bg-gray-100 active:bg-blue-50 active:text-blue-700">
                General physician
            </button>
            <button
                class="px-4 py-2 bg-white border border-gray-300 rounded-lg text-gray-700 shadow-sm hover:bg-gray-100 active:bg-blue-50 active:text-blue-700">
                Gynecologist
            </button>
            <button
                class="px-4 py-2 bg-white border border-gray-300 rounded-lg text-gray-700 shadow-sm hover:bg-gray-100 active:bg-blue-50 active:text-blue-700">
                Dermatologist
            </button>
            <button
                class="px-4 py-2 bg-white border border-gray-300 rounded-lg text-gray-700 shadow-sm hover:bg-gray-100 active:bg-blue-50 active:text-blue-700">
                Pediatricians
            </button>
            <button
                class="px-4 py-2 bg-white border border-gray-300 rounded-lg text-gray-700 shadow-sm hover:bg-gray-100 active:bg-blue-50 active:text-blue-700">
                Neurologist
            </button>
            <button
                class="px-4 py-2 bg-white border border-gray-300 rounded-lg text-gray-700 shadow-sm hover:bg-gray-100 active:bg-blue-50 active:text-blue-700">
                Gastroenterologist
            </button>
        </div>
        <!-- Doctor Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 w-full">
            <All_doctors />
        </div>
    </div>
</template>
<script setup>
import All_doctors from "./All_doctors.vue";


</script>
