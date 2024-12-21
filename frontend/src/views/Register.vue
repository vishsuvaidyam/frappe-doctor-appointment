<template>
    <div class="flex gap-10 mx-20 justify-center items-center min-h-screen bg-gradient-to-l from-sky-500 to-white  ">
    <!-- Left Section with Image -->
    <div class="w-1/2 hidden md:block ml-5">
        <img src="../assets/contact_image-IJu_19v_.png" alt="Sign Up" class="w-full h-full object-cover  " />
    </div>

    <!-- Right Section with Form -->
    <div class="w-full md:w-1/2 bg-gradient-to-r from-sky-100 to-white px-8 py-8 mr-5 shadow-lg rounded-lg">
        <h1 class="text-3xl font-bold mb-4 text-gray-800">Create Account</h1>
        <p class="text-sm text-gray-600 mb-6">
            Please sign up to book appointments
        </p>
        <form @submit.prevent="register">
            <div class="mb-4">
                <label class="block text-sm font-medium mb-1 text-gray-700">Full Name</label>
                <input v-model="full_name" type="text" class="border rounded px-4 py-3 w-full focus:outline-none focus:ring-2 focus:ring-blue-500" />
            </div>
            <div class="mb-4">
                <label class="block text-sm font-medium mb-1 text-gray-700">Email</label>
                <input v-model="email" type="email" class="border rounded px-4 py-3 w-full focus:outline-none focus:ring-2 focus:ring-blue-500" />
            </div>
            <div class="mb-4">
                <label class="block text-sm font-medium mb-1 text-gray-700">Password</label>
                <input v-model="password" type="password" class="border rounded px-4 py-3 w-full focus:outline-none focus:ring-2 focus:ring-blue-500" />
            </div>
            <button type="submit" class="w-full bg-blue-600 text-white py-3 rounded-lg mt-4 hover:bg-blue-700 transition duration-200">
                Create Account
            </button>
        </form>
        <p class="block text-sm text-gray-600 pt-4">
            Already have an account? 
            <router-link to="/login" class="text-blue-500 hover:text-blue-700">
                Login here
            </router-link>
        </p>
    </div>
</div>

</template>



<script setup>
import { inject, ref } from "vue";
const store = inject('store');
import { useRouter } from 'vue-router';


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