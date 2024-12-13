<template>
    <div class="flex justify-center items-center min-h-screen">
        <div class="bg-white p-6 shadow-md max-w-sm w-full border rounded-lg">
            <h1 class="text-2xl font-bold mb-2 text-gray-700">Create Account</h1>
            <p class="block text-sm font-medium mb-2 text-gray-600">
                Please sign up to book appointments
            </p>
            <form @submit.prevent="register">
                <div class="mb-4">
                    <label class="block text-sm font-medium mb-1">Full Name</label>
                    <input v-model="full_name" type="text" class="border rounded px-4 py-2 w-full" />
                </div>
                <div class="mb-4">
                    <label class="block text-sm font-medium mb-1">Email</label>
                    <input v-model="email" type="email" class="border rounded px-4 py-2 w-full" />
                </div>
                <div class="mb-4">
                    <label class="block text-sm font-medium mb-1">Password</label>
                    <input v-model="password" type="password" class="border rounded px-4 py-2 w-full" />
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white py-2 px-4 rounded">
                    Create Account
                </button>
            </form>
            <p class="block text-sm font-medium pt-2 text-gray-600">
                Already have an account? Login here
            </p>
        </div>
    </div>
</template>


<script setup>
import { ref } from "vue";
import axios from "axios";
// import { createResource } from 'frappe-ui';

const full_name = ref("");
const email = ref("");
const password = ref("");

// let todos = createResource({
// //   url: 'np/api/method/frappe.client.get_list',
//   params: {
//     doctype: 'Doctor',
//     filters: {
//       allocated_to: 'faris@frappe.io',
//     },
//   },
// })
// todos.fetch()

// Adjust the API endpoint to match Frappe's routing conventions
const register = async () => {
    try {
        const response = await axios.post("appointments_management.controllers.api.register_user", {
            email: email.value,
            password: password.value,
            full_name: full_name.value,
        });

        if (response.data.message === "success") {
            alert("Registration successful!");
        } else {
            alert(response.data.message || "Registration failed.");
        }
    } catch (error) {
        console.error("Registration error:", error.response?.data || error.message);
        alert("An error occurred during registration. Please try again.");
    }
};
</script>