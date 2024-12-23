<template>
    <div class="h-screen  bg-white  flex items-center justify-center px-4">
        <div class="bg-gradient-to-b from-sky-200 to-white  shadow-md rounded-2xl py-10 p-8 max-w-sm w-full">
            <h2 class="text-2xl font-extrabold   text-gray-600 text-center mb-2 "> Create Account</h2>
            <p class="text-sm font-normal text-gray-600 py-2 text-center mb-6"> Please sign up to book appointment </p>
            <form @submit.prevent="register">

                <div class="mb-4">
                    <!-- <label class="block text-sm font-medium mb-1">Full Name</label> -->
                    
                    <input v-model="full_name" type="text" class="border border-gray-300  rounded-lg px-4 py-2 w-full outline-none" placeholder="Enter your full name "/>
                    
                </div>
                <div class="mb-4">
                    <!-- <label class="block text-sm font-medium mb-1">Email</label> -->
                    <div class="mb-4 relative">
    <i class="fa-solid fa-envelope absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
    <input id="email" type="email"
        class="w-full border border-gray-300 rounded-lg pl-10 py-2 focus:outline-none"
        placeholder="Email">
</div>
                    <!-- <div class="flex justify-between">
                    <i class="fa-solid fa-envelope text-gray-400"></i>

                        <input v-model="email" type="email" class="border rounded px-4 py-2 w-full outline-none" placeholder="Enter your email" />
                    </div> -->
                </div>

                <div class="mb-4">
                    <!-- <label for="password" class="text-sm font-medium mb-1">Password</label> -->
                    <div class="mb-4 relative">
                     <i class="fa-solid fa-lock absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
                     <input id="email" type="password"
                     class="w-full border border-gray-300 rounded-lg pl-10 py-2 focus:outline-none"
                     placeholder="Password">
                </div>
                </div>
                <div class="flex justify-between items-center mb-6">
        <a href="#" class="text-sm text-blue-500 hover:underline">Forgot password?</a>
      </div>

                <button type="submit"
                    class="w-full bg-black text-white py-3 rounded-lg text-sm font-semibold hover:bg-gray-800">
                    Create Account
                </button>

                <p class="block text-sm text-gray-600 pt-4">
                    Already have an account ?
                    <router-link to="/login" class="text-blue-500 hover:text-blue-700 decoration-black">
                        Login here
                    </router-link>
                </p>
            </form>
         
            <div class="flex gap-4 pt-4 w-auto justify-center">
    <button class="flex items-center justify-center w-auto shadow-md px-9 py-2 rounded-lg border border-gray-300 ">
        <img src="https://www.google.com/favicon.ico" alt="Google" class="w-6 h-6">
    </button>

    <button class="flex items-center justify-center w-auto shadow-md px-9 py-2 rounded-lg border border-gray-300 ">
        <img src="https://www.facebook.com/favicon.ico" alt="Facebook" class="w-6 h-6">
    </button>

    <button class="flex items-center justify-center w-auto shadow-md px-9 py-2 rounded-lg border border-gray-300 ">
        <img src="https://www.apple.com/favicon.ico" alt="Apple" class="  h-6">
    </button>
</div>


        </div>
    </div>
</template>



<script setup>
import { inject, ref } from "vue";
import axios from "axios";
// const store = inject('store');
// import { useRouter } from 'vue-router';


const full_name = ref("");
const email = ref("");
const password = ref("");

const register = async () => {
    const res = await axios.get('appointments_management.controllers.api.register_user', {
        data: {
            email: email.value,
            password: password.value,
            first_name: full_name.value,
        }
    });
    console.log(res);

    if (res.code === 200) {
        alert(res.msg);
        // loading.value = false;
        // store.authPopup = false;
    } else {
        // setTimeout(() => {
        //     loading.value = false;
        // }, 1000);
        alert('This email is already associated with an account.');
    }
};


</script>