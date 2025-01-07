<!-- <template>
    <div class="inset-0 flex items-center justify-center bg-teal-100 mt-10 py-10 ">
        <div v-for=" doctor in doctorDetails" class="max-w-4xl w-full bg-white p-8 rounded-lg shadow-md">
            <h1 class="text-2xl font-bold text-center text-gray-800">Doctor Appointment Request Form</h1>
            <p class="text-center text-gray-600 mb-6">
                Fill the form below and we will get back soon to you for more updates and plan your appointment.
            </p>
            <form class="space-y-6">
                <div>
                    <label class="block text-sm font-medium text-gray-700">Name</label>
                    <div class="flex gap-4 mt-2">
                        <div class="flex-1">
                            <input v-model="patient.name" type="text" placeholder=""
                                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 outline-none" />
                            <small class="block mt-1 text-gray-500">First Name</small>
                        </div>
                        <div class="flex-1">
                            <input type="text" placeholder=""
                                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 outline-none" />
                            <small class="block mt-1 text-gray-500">Last Name</small>
                        </div>
                    </div>
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Age</label>
                    <input type="number" v-model="patient.age"
                        class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring outline-none"
                        placeholder="Enter Your Age">

                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Gender</label>
                        <select v-model="patient.gender"
                            class="mt-1 w-full p-2 border border-gray-300 rounded-md bg-white text-gray-700 focus:ring outline-none">
                            <option value="">Please Select</option>
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>

                    <div>
                        <label class="block text-sm font-medium text-gray-700">Phone Number</label>
                        <input v-model="patient.contact" type="tel" placeholder="(000) 000-0000"
                            class="mt-1 w-full p-2 border border-gray-300 rounded-md focus:ring">
                    </div>
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Address</label>
                    <textarea v-model="patient.address" type="text" placeholder="Address"
                        class="mt-1 w-full p-2 border border-gray-300 rounded-md focus:ring  outline-none"></textarea>
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Email</label>
                    <input v-model="patient.email" type="email" placeholder="example@example.com"
                        class="mt-1 w-full p-2 border  rounded-md focus:ring  outline-none">
                </div>
            </form>
            <div class="flex justify-center pt-4">
                <button class="px-6 py-2 bg-teal-500 text-white rounded-md"
                    @click=" bookAppointment(doctor.doctor.full_name, doctor.doctor.specialist, doctor.doctor.experience, doctor.doctor.doctor_image, doctor.doctor.address, doctor.doctor.doctor_fee, patient.name, patient.age, patient.gender, patient.email, date)">
                    Submit
                </button>
            </div>
        </div>
    </div>

</template>

<script setup>
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';

const route = useRoute();
const router = useRouter();
const patient = ref({
    name: '',
    gender: 'Male',
    age: '',
    contact: '',
    email: '',
    address: '',
});

const date = route.params.formattedDateTime;

const doctorDetails = ref([]);

const fetchDoctorsData = async () => {
    try {
        console.log(route.params.formattedDateTime, "=========================");
        const doctorDetailsResponse = await axios.get(
            "/api/method/appointments_management.controllers.api.doctor_details",
            {
                params: {
                    full_name: route.params.full_name,
                    specialist: route.params.specialist,
                    formattedDateTime: route.params.formattedDateTime,
                },
            }
        );

        if (doctorDetailsResponse.data.message) {
            // console.log(doctorDetailsResponse.data.message);
            doctorDetails.value = doctorDetailsResponse.data.message;
        } else {
            console.error("No data found for doctor.");
        }
    } catch (error) {
        console.error('Error fetching doctor data:', error);
    }
};


const bookAppointment = async (full_name, specialist, experience, doctor_image, address, doctor_fee, name, age, gender, email, date) => {
    console.log(date, "==============================");

    // if (!isLoggedIn.value) { 
    //         toast.error("You need to log in to book an appointment.");
    //         router.push({ name: 'Login' });  
    //         return;
    //     }
    try {
        const response = await axios.post("/api/method/appointments_management.controllers.api.appointment_data", {
            doctor_name: full_name,
            patient: name,
            specialist: specialist,
            experience: experience,
            doctor_image: doctor_image,
            address: address,
            doctor_fees: doctor_fee,
            pataient_age: age,
            gender: gender,
            email: email,
            datetime: date
        });
        if (response) {
            // console.log(response.data.message);
            router.push("/my-appointment");
        } else {
            console.log("Booking Response:", response.data);
        }

    } catch (error) {
        console.error("Error booking appointment:", error);
    }
};


onMounted(fetchDoctorsData);
</script> -->
<template>
    <div class="inset-0 flex items-center justify-center bg-opacity-50 bg-gradient-to-b from-teal-200 to-white mt-10 py-10">
        <div v-for="doctor in doctorDetails" class="max-w-4xl w-full bg-white p-8 rounded-lg shadow-md">
            <h1 class="text-2xl font-bold text-center text-gray-800">Patient Details Form</h1>
            <p class="text-center text-gray-600 mb-6">Fill the form below and we will get back to you soon for more updates and plan your appointment.</p>
            <form class="space-y-6">
                <!-- Name Input Fields -->
                <div>
                    <label class="block text-sm font-medium text-gray-700">Name</label>
                    <div class="flex gap-4 mt-2">
                        <div class="flex-1">
                            <input v-model="patient.name" type="text" :class="{ 'border-red-500': nameError }" @input="validateName" placeholder=""
                                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 outline-none" />
                            <small v-if="nameError" class="block mt-1 text-red-500">{{ nameErrorMessage }}</small>
                            <small class="block mt-1 text-gray-500">First Name</small>
                        </div>
                        <div class="flex-1">
                            <input type="text" placeholder=""
                                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 outline-none" />
                            <small class="block mt-1 text-gray-500">Last Name</small>
                        </div>
                    </div>
                </div>

                <!-- Email Input Field -->
                <div>
                    <label class="block text-sm font-medium text-gray-700">Email</label>
                    <input v-model="patient.email" type="email" :class="{ 'border-red-500': emailError }" @input="validateEmail" placeholder="example@example.com"
                        class="mt-1 w-full p-2 border rounded-md focus:ring outline-none">
                    <small v-if="emailError" class="block mt-1 text-red-500">{{ emailErrorMessage }}</small>
                </div>

                <!-- Other Form Fields -->
                <div>
                    <label class="block text-sm font-medium text-gray-700">Age</label>
                    <input type="number" v-model="patient.age" class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring outline-none" placeholder="Enter Your Age">
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Gender</label>
                        <select v-model="patient.gender"
                            class="mt-1 w-full p-2 border border-gray-300 rounded-md bg-white text-gray-700 focus:ring outline-none">
                            <option value="">Please Select</option>
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Phone Number</label>
                        <input v-model="patient.contact" type="tel" placeholder="+ 91"
                            class="mt-1 w-full p-2 border border-gray-300 rounded-md focus:ring outline-none">
                    </div>
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Address</label>
                    <textarea v-model="patient.address" type="text" placeholder="Address"
                        class="mt-1 w-full p-2 border border-gray-300 rounded-md focus:ring outline-none"></textarea>
                </div>
            </form>
            <div class="flex justify-start pt-4">
                <button class="px-20 py-2 bg-teal-500 text-white rounded-md"
                    @click="submitForm(doctor.doctor.full_name, doctor.doctor.specialist, doctor.doctor.experience, doctor.doctor.doctor_image, doctor.doctor.address, doctor.doctor.doctor_fee)">
                    Submit
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';
import { useToast } from "vue-toastification";

const toast = useToast();
const route = useRoute();
const router = useRouter();
const patient = ref({
    name: '',
    gender: '',
    age: '',
    contact: '',
    email: '',
    address: '',
});

const date = route.params.formattedDateTime;
const doctorDetails = ref([]);
const nameError = ref(false);
const nameErrorMessage = ref('');
const emailError = ref(false);
const emailErrorMessage = ref('');

const validateEmail = () => {
    const email = patient.value.email;
    const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    emailError.value = !email.match(regex);
    emailErrorMessage.value = emailError.value ? 'Please enter a valid email address.' : '';
};

const validateName = () => {
    const name = patient.value.name;
    const regex = /^[A-Za-z\s]*$/;
    nameError.value = !name.match(regex) || name.length > 40;
    nameErrorMessage.value = nameError.value
        ? name.match(regex) ? 'Name must not exceed 40 characters.' : 'Name can only contain letters and spaces.'
        : '';
};

const validationAllField = async () => {
    validateName();
    validateEmail();
    return !nameError.value && !emailError.value;
};

const submitForm = async (full_name, specialist, experience, doctor_image, address, doctor_fee, name, age, gender, email, date) => {
    const isValid = await validationAllField();
    if (!isValid) {
        toast.error("Please fix the errors before submitting.");
        return;
    }

    // Proceed with the booking
    try {
        const response = await axios.post("/api/method/appointments_management.controllers.api.appointment_data", {
            doctor_name: full_name,
            patient: name,
            specialist: specialist,
            experience: experience,
            doctor_image: doctor_image,
            address: address,
            doctor_fees: doctor_fee,
            pataient_age: age,
            gender: gender,
            email: email,
            datetime: date
        });
        if (response) {
            router.push("/my-appointment");
        } else {
            console.error("Booking Response:", response.data);
        }
    } catch (error) {
        console.error("Error booking appointment:", error);
    }
};

const fetchDoctorsData = async () => {
    try {
        const doctorDetailsResponse = await axios.get("/api/method/appointments_management.controllers.api.doctor_details", {
            params: {
                full_name: route.params.full_name,
                specialist: route.params.specialist,
                formattedDateTime: route.params.formattedDateTime,
            },
        });

        if (doctorDetailsResponse.data.message) {
            doctorDetails.value = doctorDetailsResponse.data.message;
        } else {
            console.error("No data found for doctor.");
        }
    } catch (error) {
        console.error('Error fetching doctor data:', error);
    }
};

onMounted(fetchDoctorsData);
</script>
