<template>
    <div class="h-screen  bg-gradient-to-t from-sky-200 to-white  flex items-center justify-center px-4">
        <div class="bg-white shadow-md rounded-lg p-8 max-w-sm w-full">
            <h2 class="text-2xl font-extrabold   text-gray-600 "> Create Account</h2>
            <p class="text-sm font-normal text-gray-500 py-2"> Please sign up to book appointment </p>
            <form @submit.prevent="register">

                <div class="mb-4">
                    <label class="block text-sm font-medium mb-1">Full Name</label>
                    <input v-model="full_name" type="text" class="border rounded px-4 py-2 w-full outline-none" />
                </div>
                <div class="mb-4">
                    <label class="block text-sm font-medium mb-1">Email</label>
                    <input v-model="email" type="email" class="border rounded px-4 py-2 w-full outline-none" />
                </div>

                <div class="mb-4">
                    <label for="password" class="text-sm font-medium mb-1">Password</label>
                    <input type="password" id="password" v-model="password"
                        class="border rounded px-4 py-2 w-full outline-none" placeholder="Enter your password"
                        required />
                </div>

                <button type="submit"
                    class="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition">
                    Create Account
                </button>

                <p class="block text-sm text-gray-600 pt-4">
                    Already have an account ?
                    <router-link to="/login" class="text-blue-500 hover:text-blue-700 decoration-black">
                        Login here
                    </router-link>
                </p>
            </form>

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