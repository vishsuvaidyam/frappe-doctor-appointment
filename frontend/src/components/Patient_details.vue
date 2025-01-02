<template>
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
                            placeholder="+1234567890">
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
                </div>
            </div>

            <!-- Doctor Details -->
            <div class="mt-6">
                <h3 class="text-lg font-semibold text-gray-700">Doctor Details</h3>
                <div class="space-y-2 mt-4">
                    <p><strong>Name:</strong> {{ doctor.doctor.full_name }}</p>
                    <p><strong>Specialist:</strong> {{ doctor.doctor.specialist }}{{ doctor.doctor.doctor_fee }}</p>
                </div>
            </div>
        </form>
        <router-link to="/my-appointment"
            @click=" bookAppointment(doctor.doctor.full_name, doctor.doctor.specialist ,doctor.doctor.experience, doctor.doctor.doctor_image, doctor.doctor.address, doctor.doctor.doctor_fee,patient.name,patient.age,patient.gender,patient.email)">
            Book an appointment
        </router-link>
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


const bookAppointment = async (full_name, specialist, experience, doctor_image, address, doctor_fee,name,age,gender,email) => {
    // if (!isLoggedIn.value) { 
    //         toast.error("You need to log in to book an appointment.");
    //         router.push({ name: 'Login' });  
    //         return;
    //     }
    try {
        const response = await axios.post("/api/method/appointments_management.controllers.api.appointment_data", {
            doctor_name: full_name,
            patient:name,
            specialist: specialist,
            experience: experience,
            doctor_image: doctor_image,
            address: address,
            doctor_fees:doctor_fee,
            pataient_age:age,
            gender:gender,
            email:email,
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
