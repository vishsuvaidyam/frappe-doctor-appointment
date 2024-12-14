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
import { inject, ref } from "vue";
const store = inject('store');

const full_name = ref("");
const email = ref("");
const password = ref("");

const register = async () => {
    const res = await call('appointments_management.controllers.api.register_user', {
            data: {
                email: email.value,
                password:password.value,
                first_name: full_name.value,
            }
        });

        if (res.code === 200) {
            alert(res.msg);
            loading.value = false;
            store.authPopup = false;
        } else {
            setTimeout(() => {
                loading.value = false;
            }, 1000);
            alert('This email is already associated with an account.');
        }
};


</script>