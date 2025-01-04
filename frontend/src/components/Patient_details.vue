<!-- <template>
    <div  v-for=" doctor in doctorDetails"  class="max-w-3xl mx-auto p-6 bg-white shadow-md rounded-lg mt-10">
        <h2 class="text-2xl font-bold mb-4 text-gray-800">Patient Form</h2>
        <form class="space-y-6">
            <div>
                <h3 class="text-lg font-semibold text-gray-700">Basic Information</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
                    <div>
                        <label class="block text-sm font-medium text-gray-600">Patient Name</label>
                        <input type="text" v-model="patient.name"
                            class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200"
                            placeholder="Enter Your Patient Name">
                    </div>
                    <div>
                        <label class="block text-sm font-medium">Gender</label>
                        <select v-model="patient.gender"
                            class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200">
                            <option>Male</option>
                            <option>Female</option>
                            <option>Other</option>
                        </select>
                    </div>

                    <div>
                        <label class="block text-sm font-medium text-gray-600">Age</label>
                        <input type="number" v-model="patient.age"
                            class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200"
                            placeholder="Enter Your Age">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-600">Contact Number</label>
                        <input type="tel" v-model="patient.contact"
                            class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200"
                            placeholder="+911234567890">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-600">Email</label>
                        <input type="email" v-model="patient.email"
                            class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200"
                            placeholder="Enter Your Email">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-600">Address</label>
                        <textarea v-model="patient.address"
                            class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200"
                            placeholder="Enter Your Address" rows="4"></textarea>
                    </div>
                </div> -->
<!-- <div class="mt-8 flex justify-centv-for=" doctor in doctorDetails" er">
                    <button type="submit"
                        class="w-80 px-4 py-2 text-white bg-indigo-600 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500">
                        Submit
                    </button>
                </div> -->
<!-- </div>
        </form>
        <router-link to="/my-appointment"
            @click=" bookAppointment(doctor.doctor.full_name, doctor.doctor.specialist ,doctor.doctor.experience, doctor.doctor.doctor_image, doctor.doctor.address, doctor.doctor.doctor_fee,patient.name,patient.age,patient.gender,patient.email)">
            Book an appointment
        </router-link>
    </div> -->

<!-- </template> -->
<template>
    <div class="min-h-screen flex items-center justify-center bg-teal-100">
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
                            <option>Please Select</option>
                            <option>Male</option>
                            <option>Female</option>
                            <option>Other</option>
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
            <div class="flex justify-center pt-4" >
                <router-link to="/my-appointment" class="px-6 py-2 bg-teal-500 text-white rounded-md"
                    @click=" bookAppointment(doctor.doctor.full_name, doctor.doctor.specialist, doctor.doctor.experience, doctor.doctor.doctor_image, doctor.doctor.address, doctor.doctor.doctor_fee, patient.name, patient.age, patient.gender, patient.email)">
                    Submit
                </router-link>
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

console.log(patient);

const doctorDetails = ref([]);

const fetchDoctorsData = async () => {
    try {
        const doctorDetailsResponse = await axios.get(
            "/api/method/appointments_management.controllers.api.doctor_details",
            {
                params: {
                    full_name: route.params.full_name,
                    specialist: route.params.specialist,
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


const bookAppointment = async (full_name, specialist, experience, doctor_image, address, doctor_fee, name, age, gender, email) => {
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
        });
        console.log(response);

        if (response) {
            console.log(response.data.message);
            // router.push({
            //     name: "/My_appointments",
            // });
            // toast.success("Appointment booked successfully!");
        } else {
            console.log("Booking Response:", response.data);
        }



    } catch (error) {
        console.error("Error booking appointment:", error);
    }
};


onMounted(fetchDoctorsData);
</script>
