<template>
    <div>
        <h2 class="text-lg font-semibold pt-4">Related Doctors</h2>
        <div class="grid grid-cols-3 gap-6 mt-4">
            <div v-for="doctor in relatedDoctors" :key="doctor.name" class="border p-4 rounded-lg">
                <img class="w-full h-40 object-cover rounded-md" :src="doctor.doctor_image" alt="Doctor Image" />
                <h3 class="mt-2 text-lg font-semibold">{{ doctor.name }}</h3>
                <p class="text-sm text-gray-600">{{ doctor.qulifications }} - {{ doctor.specialist }}</p>
                <p class="text-sm text-gray-600">Experience: {{ doctor.experience }}</p>
                <p class="text-sm text-gray-600">Fee: ${{ doctor.doctor_fee }}</p>
            </div>
        </div>
    </div>
</template>

<!-- <script setup>
defineProps(['relatedDoctors']);
</script> -->
<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';

const relatedDoctors = ref([]);

const fetchRelatedDoctors = async (specialist) => {
    try {
        const response = await axios.get(
            `/api/method/appointments_management.controllers.api.related_doctors`,
            { params: { specialist } } // Pass `specialist` as a query parameter
        );
        if (response.data.message) {
            relatedDoctors.value = response.data.message;
            console.log("Related Doctors:", relatedDoctors.value);
        } else {
            console.error("No related doctors found.");
        }
    } catch (error) {
        console.error('Error fetching related doctors:', error);
    }
};


// Fetch related doctors when doctorDetails is updated
const doctorDetails = ref([]);
const Doctordatails = async () => {
    // ... existing code to fetch doctor details
    if (doctorDetails.value[0]?.specialist) {
        fetchRelatedDoctors(doctorDetails.value[0].specialist);
    }
};

onMounted(Doctordatails);
</script>
