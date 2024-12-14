<template>
    <div class="flex flex-col md:flex-row gap-4 p-6 bg-gray-50 mx-20 h-auto">
     <div class="flex flex-col gap-2 p-4 w-64">
    <button
        class="w-full pr-10 py-2 bg-white border border-gray-300 rounded-sm text-gray-700 shadow-sm hover:bg-gray-100 active:bg-blue-50 active:text-blue-700">
        General physician
    </button>
    <button
        class="w-full pr-16 py-2 bg-white border border-gray-300 rounded-sm text-gray-700 shadow-sm hover:bg-gray-100 active:bg-blue-50 active:text-blue-700">
        Gynecologist
    </button>
    <button
        class="w-full pr-14 py-2 bg-white border border-gray-300 rounded-sm text-gray-700 shadow-sm hover:bg-gray-100 active:bg-blue-50 active:text-blue-700">
        Dermatologist
    </button>
    <button
        class="w-full pr-14 py-2 bg-white border border-gray-300 rounded-sm text-gray-700 shadow-sm hover:bg-gray-100 active:bg-blue-50 active:text-blue-700">
        Pediatricians
    </button>
    <button
        class="w-full pr-16 py-2 bg-white border border-gray-300 rounded-sm text-gray-700 shadow-sm hover:bg-gray-100 active:bg-blue-50 active:text-blue-700">
        Neurologist
    </button>
    <button
        class="w-full pr-6 py-2 bg-white border border-gray-300 rounded-sm text-gray-700 shadow-sm hover:bg-gray-100 active:bg-blue-50 active:text-blue-700">
        Gastroenterologist
    </button>
</div>

       
        <!-- Doctor Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-6 w-full">
            <All_doctors />
        </div>
    </div>
</template>
<script setup>
import All_doctors from "./All_doctors.vue";


</script>
