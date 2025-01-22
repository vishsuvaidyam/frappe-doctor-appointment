<template>
    <div class="fixed inset-0 flex justify-center items-center bg-white">
        <div class="opacity-85 fixed inset-0 bg-black bg-opacity-50"></div>
        <div class="relative z-50 bg-gray-50 opacity-85 border px-4 h-90 w-1/2 pt-5 sm:p-6 sm:pb-4">
            <div class="block justify-center gap-5 items-center"></div>
            <div class="space-y-6 container">
                <div>
                    <input v-model="email" id="email" type="email" placeholder="Enter email address"
                        class="w-full px-3 py-2.5 border-b bg-gray-100 placeholder:text-[#697077] border-gray-300 shadow-sm outline-none" />
                    <input v-model="password_new" id="password" type="password" placeholder="Enter new password"
                        class="w-full px-3 py-2.5 mt-4 border-b bg-gray-100 placeholder:text-[#697077] border-gray-300 shadow-sm outline-none" />
                </div>
                <div class="flex flex-col items-center gap-2 justify-center">
                    <button @click="reset_password"
                        class="w-full py-2 px-8 rounded-md flex bg-[#245da2] text-white items-center justify-center gap-2">
                        Reset Password
                    </button>
                    <router-link to="/login" class="text-sm font-normal cursor-pointer text-black">
                        Back to Login
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue";
import { useToast } from "vue-toastification";
import axios from "axios";
import { useRouter } from "vue-router";

const router=useRouter();
const email = ref("");
const password_new = ref("");
const toast = useToast();

const reset_password = async () => {
    if (!email.value || !password_new.value) {
        toast.error("Please fill in both email and password.");
        return;
    }

    try {
        const response = await axios.post(
            "/api/method/appointments_management.controllers.api.set_new_password",
            {
                email: email.value,
                new_password: password_new.value,
            }
        );
        const result = response.data;
            console.log(result);
            
        if (result.message.code  === 200) {
            toast.success(result.message.message);
            router.push("/login");
        } else if (result.message.code  === 404) {
            toast.error(result.message.message);
        } else {
            toast.error(result.message.message);
        }
    } catch (error) {
        const errorMessage =
            error.response?.data?.message || "An unexpected error occurred.";
        toast.error(`Error: ${errorMessage}`);
        console.error("Reset password error:", error);
    }
};
</script>