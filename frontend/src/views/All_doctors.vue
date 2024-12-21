<template>
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
</template>


<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
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

const goToDoctorDetails = (full_name) => {
    router.push({ name: 'Doctor_details', params: { full_name: full_name } });

};
onMounted(fetchDoctorsData);

</script>