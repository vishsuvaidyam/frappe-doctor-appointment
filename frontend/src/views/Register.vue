<template>
    <div class="h-screen bg-gradient-to-b from-sky-200 to-white bg-white flex items-center justify-center px-4">
        <div class=" shadow-md rounded-lg bg-white py-10 p-8 max-w-sm w-full">
            <h2 class="text-2xl font-extrabold text-gray-600 text-center mb-2">Create Account</h2>
            <p class="text-sm font-normal text-gray-600 py-2 text-center mb-6">Please sign up to book an appointment</p>
            <form @submit.prevent="register">

                <div class="mb-4">
                    <div class="relative">
                        <!-- <i class="fa-solid fa-envelope absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i> -->
                        <svg xmlns="http://www.w3.org/2000/svg"
                            class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 h-6 w-"
                            fill="currentColor" viewBox="0 0 24 24">
                            <path
                                d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-3.86 0-7 3.14-7 7h14c0-3.86-3.14-7-7-7z" />
                        </svg>

                        <input v-model="full_name" type="text"
                            class="w-full border border-gray-300 rounded-lg pl-10 py-2 focus:outline-none"
                            placeholder="Name" />
                    </div>
                </div>
                <div class="mb-4">
                    <div class="relative">
                        <i
                            class="fa-solid fa-envelope absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
                        <input v-model="email" type="email"
                            class="w-full border border-gray-300 rounded-lg pl-10 py-2 focus:outline-none"
                            placeholder="Email" />
                    </div>
                </div>
                <div class="mb-4">
                    <div class="relative">
                        <i
                            class="fa-solid fa-lock absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
                        <input v-model="password" type="password"
                            class="w-full border border-gray-300 rounded-lg pl-10 py-2 focus:outline-none"
                            placeholder="Password" />
                    </div>
                </div>
                <div class="flex justify-end items-center mb-4">
                    <a href="#" class="text-sm text-blue-500 hover:underline ">Forgot password?</a>
                </div>

                <button type="submit"
                    class="w-full bg-black text-white py-3 rounded-lg text-sm font-semibold hover:bg-gray-800">
                    Create Account
                </button>

                <p class="block text-sm text-gray-600 pt-4">
                    Already have an account?
                    <router-link to="/login" class="text-blue-500 hover:text-blue-700 decoration-black">
                        Login here
                    </router-link>
                </p>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useToast } from "vue-toastification";

const toast = useToast();
const full_name = ref("");
const email = ref("");
const password = ref("");

const register = async () => {
    try {
        const res = await axios.post("/api/method/appointments_management.controllers.api.register_user", {
            email: email.value,
            password: password.value,
            first_name: full_name.value,
        });

        if (res.data.message.code === 200) {
            toast.success("registered successfully");
            email.value = '';
            password.value = '';
            full_name.value = '';

        } else if (res.data.message.code === 400) {
            toast.error("User already exists");
        } else {
            toast.error("An unexpected error occurred. Please try again.");
        }
    } catch (error) {
        console.error(error);
        toast.error("An error occurred while registering the user. Please try again.");
    }

}
</script>
