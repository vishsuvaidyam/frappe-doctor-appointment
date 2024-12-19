<template>
    <div class="w-full h-auto">
        <section class="text-center py-12">
            <h1 class="text-3xl font-bold">Find by Speciality</h1>
            <p class="text-gray-500 mt-2">
                Simply browse through our extensive list of trusted doctors, schedule your appointment hassle-free.
            </p>

            <div v-if="doctors.length" class="mt-8 flex flex-wrap justify-center gap-6 cursor-pointer ">
                <div v-for="doctor in doctors" :key="doctor.name1" @click="handleClick(doctor.name1)">
                    <div class="flex flex-col items-center">
                        <div class="w-20 h-20 bg-blue-100 rounded-full flex items-center justify-center">
                            <img :src="doctor.image" alt="Doctor Image" />
                        </div>
                        <p class="mt-2 text-sm text-gray-700">{{ doctor.name }}</p>
                    </div>
                </div>
            </div>

            <!-- <div class="relative inline-block text-left">
                <button @click="isOpen = !isOpen"
                    class="inline-flex justify-center w-full rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50">
                    Click me
                </button>

                <div v-if="isOpen"
                    class="absolute right-0 mt-2 w-56 origin-top-right rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none">
                    <div class="p-4 text-gray-700">
                        Popover content
                    </div>
                </div>
            </div> -->
        </section>

    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

// const isOpen = ref(false);
const doctors = ref([]);
const apiResponse = ref(null);
const router = useRouter();

const fetchDoctorsData = async () => {
    try {
        const response = await axios.get('api/method/appointments_management.controllers.api.spaclist');
        const data = response.data;
        if (data.message) {
            doctors.value = data.message;
        } else {
            console.error("Expected an array, but got:", data);
        }
    } catch (error) {
        console.error('Error fetching doctors data:', error);
    }
};

const handleClick = async (id) => {

    try {
        const responses = await axios.get(
            `/api/method/appointments_management.controllers.api.doctors_filter?id=${encodeURIComponent(id)}`
        );
        console.log('API Response:', responses);

        const data = responses.data;
        if (!data || !data.message) {
            throw new Error('API call failed or returned invalid data');
        }
        apiResponse.value = data.message;
        console.log('API response (filtered doctors):', apiResponse.value);

        // router.push({
        //     name: 'Doctors',
        // });
    } catch (error) {
        console.error('Error during API call:', error);
    }
};

onMounted(fetchDoctorsData);
</script>
