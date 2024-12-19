<template>
    <div v-for="(doctor, index) in doctors" :key="index"
        class="bg-white shadow-md rounded-lg border-t-4 border-blue-500 p-6 text-start cursor-pointer" @click="details_doctors(full_name)">
        <div class="">
            <img class="w-full h-54 mx-auto " :src="doctor.doctor_image"
            :alt="`${doctor.full_name[0]}`">
        </div>
        <div class="mt-4">
            <span :class="{
                'text-green-500': doctor.status === 'Available',
                'text-red-500': doctor.status !== 'Available',
            }" class="text-sm font-medium">● {{ doctor.status }}</span>
            <h3 class="text-lg font-semibold text-gray-800 mt-2">{{ doctor.full_name }}</h3>
            <p class="text-sm text-gray-600">{{ doctor.specialist }}</p>
        </div>
    </div>

</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
const doctors = ref([]);
const fetchDoctorsData = async () => {
    try {
        const response = await axios.get('api/method/appointments_management.controllers.api.doctors_data');
        const data = await response.data;
        if (data.message.length) {
            doctors.value = data.message;
        } else {
            console.error("Expected an array, but got:", data);
        }
    } catch (error) {
        console.error('Error fetching doctors data:', error);
    }
};

const details_doctors=async (full_name)=> {
    try{
        const a=await axios.get(`/api/method/appointments_management.controllers.api.doctor_details?full_name=${encodeURIComponent(full_name)}`);
        const d=await a.message;
        if(d){
            console.log(d);
            s.value=d.message
        }
    }catch(error){
        console.log('error');
        
    }
}

onMounted(fetchDoctorsData);

</script>
 