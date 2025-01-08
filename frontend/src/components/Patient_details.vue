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
                            <input v-model="patient.name" type="text" :class="{ 'border-red-500': nameError }"
                                @input="validateName" placeholder=""
                                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" />
                            <small v-if="nameError" class="block mt-1 text-red-500">{{ nameErrorMessage }}</small>
                            <small class="block mt-1 text-gray-500">First Name</small>
                        </div>
                        <div class="flex-1">
                            <input v-model="patient.lastname" type="text" placeholder=""
                                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" />
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
    <div
        class="inset-0 flex items-center justify-center bg-opacity-50 bg-gradient-to-b from-teal-200 to-white mt-10 py-10">
        <div v-for="doctor in doctorDetails" :key="doctor.doctor.full_name"
            class="max-w-4xl w-full bg-white p-8 py-12 rounded-lg shadow-md">
            <h1 class="text-2xl font-bold text-center text-gray-800">Patient Details Form</h1>
            <p class="text-center text-gray-600 mb-6">Fill the form below and we will get back to you soon for more
                updates and plan your appointment.</p>
            <form class="space-y-6">
                <!-- Name Input Fields -->
                <div>
                    <label class="block text-sm font-medium text-gray-700">Name</label>
                    <div class="flex gap-4 mt-2">
                        <div class="flex-1">
                            <input v-model="patient.name" type="text" :class="{ 'border-red-500': nameError }"
                                @input="validateName" placeholder=""
                                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" />
                            <small v-if="nameError" class="block mt-1 text-red-500">{{ nameErrorMessage }}</small>
                            <small class="block mt-1 text-gray-500">First Name</small>
                        </div>
                        <div class="flex-1">
                            <input v-model="patient.lastname" type="text" placeholder=""
                                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" />
                            <small class="block mt-1 text-gray-500">Last Name</small>
                        </div>
                    </div>
                </div>

                <!-- Email Input Field -->
                <div class="flex gap-4">
                    <div class="flex-1">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
                        <input v-model="patient.email" type="email" :class="{ 'border-red-500': emailError }"
                            @input="validateEmail"
                            class="w-full px-4 py-2 border border-gray-300 rounded-md  focus:ring outline-none"
                            placeholder="example@example.com" />
                        <small v-if="emailError" class="text-red-500">{{ emailErrorMessage }}</small>
                    </div>
                    <div class="flex-1">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Age</label>
                        <input type="text" v-model="patient.age" :class="{ 'border-red-500': ageError }"
                            class="w-full px-4 py-2 border border-gray-300 rounded-md  focus:ring outline-none"
                            placeholder="Enter Your Age" @input="validateAge" />
                        <small v-if="ageError" class="text-red-500">{{ ageErrorMessage }}</small>
                    </div>
                </div>
                <!-- Gender and Phone Number -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Gender</label>
                        <select v-model="patient.gender" @change="validateGender"
                            class="mt-1 w-full py-2 px-2 border border-gray-300 rounded-md bg-white text-gray-700 focus:ring outline-none"
                            :class="{ 'border-red-500': genderError }">
                            <option value="">Please Select</option>
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                            <option value="Other">Other</option>
                        </select>
                        <small v-if="genderError" class="text-red-500 text-sm mt-1">{{ genderError }}</small>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Phone Number</label>
                        <input v-model="patient.contact" type="tel" placeholder="+91"
                            class="mt-1 w-full p-2 border border-gray-300 rounded-md focus:ring outline-none"
                            :class="{ 'border-red-500': phoneError }" @input="validatePhoneNumber" />
                        <small v-if="phoneError" class="text-red-500 text-sm mt-1">{{ phoneError }}</small>
                    </div>
                </div>

                <!-- Address Field -->
                <div>
                    <label class="block text-sm font-medium text-gray-700">Address</label>
                    <textarea v-model="patient.address" placeholder="Enter your address"
                        class="mt-1 w-full p-2 h-20 border border-gray-300 rounded-md focus:ring outline-none"
                        :class="{ 'border-red-500': addressError }"></textarea>
                    <small v-if="addressError" class="block mt-1 text-red-500">{{ addressErrorMessage }}</small>
                </div>
            </form>
            <div class="flex justify-center pt-8">
                <button type="submit" class="px-20 w-full py-2 bg-teal-500 text-white rounded-md"
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
import { ref, reactive, onMounted } from 'vue';
import { useToast } from "vue-toastification";

const toast = useToast();
const route = useRoute();
const router = useRouter();
const patient = reactive({
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
const ageError = ref(false);
const ageErrorMessage = ref("");
const phoneError = ref('');
const genderError = ref('');
const addressErrorMessage = ref('');
const addressError = ref(false);

const validateEmail = () => {
    const email = patient.email;
    const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    emailError.value = !email.match(regex);
    emailErrorMessage.value = emailError.value ? 'Please enter a valid email address.' : '';
};

const validateName = () => {
    const name = patient.name.trim();
    const regex = /^[A-Za-z\s]+$/;
    const isValidName = regex.test(name) && name.length <= 40;
    nameError.value = !isValidName;
    nameErrorMessage.value = nameError.value
        ? !regex.test(name)
            ? 'Name can only contain letters and spaces.'
            : 'Name must not exceed 40 characters.'
        : '';
};

const validateAge = () => {
    const age = patient.age;

    if (age === "" || age == null) {
        ageError.value = true;
        ageErrorMessage.value = "Age is required.";
    } else if (age <= 0) {
        ageError.value = true;
        ageErrorMessage.value = "Age must be a positive number.";
    } else if (age < 10 || age > 95) {
        ageError.value = true;
        ageErrorMessage.value = "Please enter a valid age between 10 and 95.";
    } else {
        ageError.value = false;
        ageErrorMessage.value = "";
    }
};

const validateGender = () => {
    if (!patient.gender) {
        genderError.value = 'Gender is required.';
    } else {
        genderError.value = '';
    }
};

const validatePhoneNumber = () => {
    const phoneRegex = /^[6-9]\d{9}$/;
    const phone = patient.contact.trim();
    if (!phone) {
        phoneError.value = 'Phone number is required.';
        return false;
    }
    if (phone.length !== 10) {
        phoneError.value = 'Phone number must be exactly 10 digits.';
        return false;
    }
    if (!phoneRegex.test(phone)) {
        phoneError.value = 'Enter a valid phone number (e.g., 9876543210).';
        return false;
    }
    phoneError.value = '';
    return true;
};


const validateAddress = () => {
    const address = patient.address.trim();
    if (!address) {
        addressError.value = true;
        addressErrorMessage.value = "Address is required.";
    } else {
        addressError.value = false;
        addressErrorMessage.value = "";
    }
};

const validationAllField = async () => {
    validateName();
    validateEmail();
    validateAge();
    validateGender();
    validatePhoneNumber();
    validateAddress();
    return !nameError.value && !emailError.value && !ageError.value && !genderError.value && !phoneError.value && !addressError.value;
};

const bookAppointment = async (full_name, specialist, experience, doctor_image, address, doctor_fee, name, age, gender, email, date) => {
    const isValid = await validationAllField();
    if (!isValid) {
        toast.error("Please fix the errors in the form.");
        return;
    }

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
            toast.success("Appointment Successfully!")
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
