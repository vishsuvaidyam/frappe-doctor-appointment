<template>
    <div v-for="(doctor, index) in doctors" :key="index"
        class="bg-white shadow-md rounded-lg border-t-4 border-blue-500 p-6 text-center">
        <div>
            <img class="w-full h-54 mx-auto " :src="doctor.image"
            :alt="`Image of ${doctor.name}`">

        </div>
        
        <div class="mt-4">
            <span class="text-green-500 text-sm font-medium">● Available</span>
            <h3 class="text-lg font-semibold text-gray-800 mt-2">{{ doctor.name }}</h3>
            <p class="text-sm text-gray-600">{{ doctor.specialty }}</p>
        </div>
    </div>
</template>
<script setup>
import doc1 from "../assets/doc1.png";

const doctors = [
    { name: "Dr. Richard James", specialty: "General Physician", image: doc1 },
    { name: "Dr. Richard James", specialty: "General Physician", image: doc1 },
    { name: "Dr. Richard James", specialty: "General Physician", image: doc1 },
    { name: "Dr. Richard James", specialty: "General Physician", image: doc1 },
    { name: "Dr. Richard James", specialty: "General Physician", image: doc1 },
    { name: "Dr. Richard James", specialty: "General Physician", image: doc1 },
    { name: "Dr. Richard James", specialty: "General Physician", image: doc1 },
    { name: "Dr. Richard James", specialty: "General Physician", image: doc1 },
    { name: "Dr. Richard James", specialty: "General Physician", image: doc1 },
    { name: "Dr. Richard James", specialty: "General Physician", image: doc1 },
];




</script>
