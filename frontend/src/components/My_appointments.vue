<template>
    <div class="mx-auto mt-4">
        <h2 class="text-xl font-semibold mb-2">My Appointments</h2>
        <div v-for="doctorappointment in doctorappoint" :key="doctorappointment.id"
            class="flex items-start p-4 border rounded-lg shadow-sm">
            <img class="w-36 h-30 object-cover rounded-md border" :src="doctorappointment.doctor_image" alt="Doctor" />
            <div class="flex-1 ml-6">
                <h3 class="text-lg font-bold">{{ doctorappointment.name }}</h3>
                <p class="text-sm text-gray-600">{{ doctorappointment.specialist }}</p>
                <p class="text-sm text-gray-600">
                    <span class="font-semibold">Address: <br> </span>
                    {{ doctorappointment.address }}
                </p>
                <p class="text-sm text-gray-600">
                    <span class="font-semibold">Date & Time:</span>{{ selectedDate }}
                </p>
            </div>
            <div class="flex flex-col space-y-3 py-8">
                <button class="bg-gray-100 text-black text-sm py-2 px-4 rounded-lg hover:bg-blue-600 hover:text-white"
                    @click="payOnline">
                    Pay Online
                </button>
                <button class="bg-gray-100 text-sm py-2 px-4 rounded-lg hover:bg-red-500 hover:text-white"
                    @click="cancelAppointment">
                    Cancel Appointment
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';

const toast = useToast();
const route = useRoute();
const router = useRouter();
const selectedDate = route.query.date || "N/A";
const doctorappoint = ref([]);

// Function to check if the user is logged in
const checkLogin = async () => {
    try {
        const response = await axios.get("/api/method/appointments_management.controllers.api.login_user");
        return response.data.login_user;
    } catch (error) {
        console.error("Error checking login status:", error);
        return false;
    }
};

const appointment = async () => {
    console.log("Route Param Full Name:", route.params.full_name);
    try {
        const loggedIn = await checkLogin();

        if (!loggedIn) {
            toast.error("You must be logged in to book an appointment.");
            router.push({ name: 'LoginPage' }); // Redirect to the login page
            return;
        }

        const response = await axios.get(
            "/api/method/appointments_management.controllers.api.details",
            {
                params: {
                    full_name: route.params.full_name || "",
                },
            }
        );

        if (response.data.message) {
            doctorappoint.value = response.data.message;
            toast.success("Appointment Booked");
            console.log("Doctor Details Fetched:", doctorappoint.value);
        } else {
            console.error("No data found for doctor.");
        }
    } catch (error) {
        console.error("Error fetching doctor details:", error);
    }
};

onMounted(appointment);
</script>