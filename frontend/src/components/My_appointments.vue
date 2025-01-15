<template>
    <div class="mx-auto mt-4 px-4 sm:px-6 md:px-10">
        <h2 class="text-lg sm:text-xl font-semibold mb-2">My Appointments</h2>
        <div v-for="(doctorappointment, index) in doctorappoint" :key="doctorappointment.id"
            class="flex flex-col sm:flex-row items-start p-4 border rounded-lg mb-4">
            <div class="w-24 h-24 sm:w-36 sm:h-36 border border-gray-300 bg-gray-100 rounded-md overflow-hidden">
                <img class="w-full h-full object-cover" :src="doctorappointment.doctor_image"
                    :alt="doctorappointment.doctor_name[0]" />
            </div>

            <div class="flex-1 ml-0 sm:ml-6 mt-4 sm:mt-0">
                <h3 class="text-md sm:text-lg font-bold">
                    {{ doctorappointment.doctor_name }}
                </h3>
                <p class="text-sm text-gray-600">{{ doctorappointment.specialist }}</p>
                <p class="text-sm text-gray-600 mt-1">
                    <span class="font-semibold">Address:</span><br />
                    <span class="text-gray-500 inline-block break-words w-full sm:w-48">
                        {{ doctorappointment.address }}
                    </span>
                </p>
                <p class="text-sm text-gray-600 mt-1">
                    <span class="font-semibold">Date & Time:</span> {{ doctorappointment.datetime }}
                </p>
            </div>

            <div class="button-container flex flex-col space-y-3 py-4 sm:py-8 mt-4 sm:mt-0">
                <!-- Payment Section -->
                <div v-if="!doctorappointment.canceled">
                    <!-- <div v-if="doctorappointment.isPaymentVisible" class="payment-section">
                        <button class="hover:bg-gray-100 border text-black text-sm py-2 px-8 sm:px-14"
                            @click="initiatePayment(index)">
                            <img class="h-6" src="../assets/Stript.png" alt="Stripe Logo">
                        </button>
                    </div>
                    <div v-if="doctorappointment.isPaymentVisible" class="payment-section pt-2">
                        <button class="hover:bg-gray-100 border text-black text-sm py-2 px-6 sm:px-9">
                            <img class="h-5" src="../assets/Razopay.png" alt="Razorpay Logo">
                        </button>
                    </div> -->
                    <button  
                        class="border text-black text-sm py-2 px-12 sm:px-16 hover:bg-blue-600 hover:text-white"
                        @click="showPaymentOptions(index)">
                        Pay Online
                    </button>
                </div>

                <!-- Cancel Button -->
                <button v-if="!doctorappointment.canceled"
                    class="border text-black font-normal text-sm py-2 px-4 hover:bg-red-500 hover:text-white"
                    @click="cancelAppointment(index)">
                    Cancel Appointment
                </button>

                <!-- Appointment Canceled -->
                <div v-if="doctorappointment.canceled">
                    <button class="border border-red-500 text-red-500 font-normal text-sm py-2 px-4 my-6" disabled>
                        Appointment Canceled
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import {useRouter} from "vue-router";
import axios from "axios";


// Replace with your provided Stripe public key
// const stripePromise = loadStripe("pk_test_51QeDoT079z0KEg54NoLl3UrSsd2HGv7TYOuKfThvVmn4XASwpB2T6TrxRVb3B8j9aGTriJjyUvEDVtXmcBTfqLgN00iUIPr4sY");
const router = useRouter();
const doctorappoint = ref([]);

const fetchAppointments = async () => {
    try {
        const response = await axios.get(
            "/api/method/appointments_management.controllers.api.my_appointment"
        );
        if (response.data.message) {
            doctorappoint.value = response.data.message.map(appointment => ({
                ...appointment,
                canceled: false,
                isPaymentVisible: false,
            }));
        }
    } catch (error) {
        console.error("Error fetching appointments:", error);
    }
};

const showPaymentOptions = (index) => {
    // doctorappoint.value[index].isPaymentVisible = true;
    router.push("/otheracount")
};

const cancelAppointment = async (index) => {
    try {
        // Update the status in Frappe to "Canceled"
        const appointmentId = doctorappoint.value[index].id;

        const response = await axios.post("/api/method/appointments_management.controllers.api.set_status_canceled", {
            appointment_id: appointmentId,
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (response.data.message) {
            alert(response.data.message);  // Show confirmation message
            doctorappoint.value[index].canceled = true; // Mark appointment as canceled
        }
    } catch (error) {
        console.error("Error canceling appointment:", error);
    }
};

const initiatePayment = async (index) => {
    try {
        const stripe = await stripePromise;
        const appointment = doctorappoint.value[index];

        // Send a request to your backend to create a payment session
        const response = await axios.post("/api/method/appointments_management.controllers.api.create-payment-session", {
            appointmentId: appointment.id,
        });

        // Redirect to Stripe Checkout
        const { sessionId } = response.data;
        await stripe.redirectToCheckout({ sessionId });
    } catch (error) {
        console.error("Error initiating payment:", error);
    }
};

onMounted(fetchAppointments);
</script>
