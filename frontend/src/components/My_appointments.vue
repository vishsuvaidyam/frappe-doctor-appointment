<template>
    <div class="mx-auto mt-4 px-4 sm:px-6 md:px-10">
        <h2 class="text-lg sm:text-xl font-semibold mb-2">My Appointments</h2>
        <div v-for="doctorappointment in doctorappoint" :key="doctorappointment.id"
            class="flex flex-col sm:flex-row items-start p-4 border rounded-lg mb-4">
            <div class="w-24 h-24 sm:w-36 sm:h-36 border border-gray-300 bg-gray-100 rounded-md overflow-hidden">
                <img class="w-full h-full object-cover" :src="doctorappointment.doctor_image"
                    :alt="doctorappointment.name[0]" />
            </div>

            <div class="flex-1 ml-0 sm:ml-6 mt-4 sm:mt-0">
                <h3 class="text-md sm:text-lg font-bold">{{ doctorappointment.name }}</h3>
                <p class="text-sm text-gray-600">{{ doctorappointment.specialist }}</p>
                <p class="text-sm text-gray-600 mt-1">
                    <span class="font-semibold">Address:</span><br>
                    <span class="text-gray-500 inline-block break-words w-full sm:w-48">
                        {{ doctorappointment.address }}
                    </span>
                </p>

                <p class="text-sm text-gray-600 mt-1">
                    <span class="font-semibold">Date & Time:</span> {{ selectedDate }}
                </p>
            </div>
            <div class="flex flex-col space-y-3 py-4 sm:py-8 mt-4 sm:mt-0">
                <div v-if="!cancle">
                    <div v-if="isPaymentVisible" class="payment-section">
                        <button class="hover:bg-gray-100 border text-black text-sm py-2 px-8 sm:px-14">
                            <img class="h-6" src="../assets/Stript.png" alt="Stripe Logo">
                        </button>
                    </div>
                    <div v-if="isPaymentVisible" class="payment-section pt-2">
                        <button class="hover:bg-gray-100 border text-black text-sm py-2 px-6 sm:px-9">
                            <img class="h-5" src="../assets/Razopay.png" alt="Razorpay Logo">
                        </button>
                    </div>
                    <button v-if="!isPaymentVisible" :class="hidden"
                        class="border text-black text-sm py-2 px-12 sm:px-16 hover:bg-blue-600 hover:text-white"
                        @click="payOnline">
                        Pay Online
                    </button>
                </div>

                <button v-if="!cancle"
                    class="border text-gray-500 font-normal text-sm py-2 px-4 hover:bg-red-500 hover:text-white"
                    @click="Cancelappointment">
                    Cancel Appointment
                </button>

                <div v-if="cancle">
                    <button class="border border-red-500 text-red-500 font-normal text-sm py-2 px-4 my-6"
                        @click="Cancelappointment">
                        Appointment Canceled
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';

const isPaymentVisible = ref()
const cancle = ref()
const toast = useToast();
const route = useRoute();
const router = useRouter();
const selectedDate = route.query.date || "N/A";
const doctorappoint = ref([]);

const appointment = async () => {
    console.log("Route Param Full Name:", route.params.full_name);
    try {
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
        } else {
            console.error("No data found for doctor.");
        }
    } catch (error) {
        console.error("Error fetching doctor details:", error);
    }
};

const payOnline = () => {
    isPaymentVisible.value = true
}

const Cancelappointment = () => {
    cancle.value = true;
};
onMounted(appointment);
</script>
