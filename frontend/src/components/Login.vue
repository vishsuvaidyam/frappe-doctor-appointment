<template>
    <div class="flex justify-center items-center min-h-screen bg-gray-100">
        <div class="bg-white p-6 rounded shadow-md max-w-sm w-full">
            <h1 class="text-2xl font-bold mb-4">Login</h1>
            <form @submit.prevent="handleLogin">
                <div class="mb-4">
                    <label class="block text-sm font-medium mb-1">Email</label>
                    <input v-model="email" type="email" class="border rounded px-4 py-2 w-full" />
                </div>
                <div class="mb-4">
                    <label class="block text-sm font-medium mb-1">Password</label>
                    <input v-model="password" type="password" class="border rounded px-4 py-2 w-full" />
                </div>
                <button type="submit" class="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
                    Login
                </button>
            </form>
            <button @click="showPopUp" class="mt-4 w-full bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-600">
                Open Pop-up
            </button>
        </div>

        <Modal v-if="isModalOpen" :isOpen="isModalOpen" title="Hello Modal" @close="closeModal">
            <p>This is a sample pop-up modal.</p>
            <button @click="closeModal" class="mt-4 bg-red-500 text-white py-2 px-4 rounded hover:bg-red-600">
                Close
            </button>
        </Modal>
    </div>
</template>

<script>
import Modal from './Modal.vue';

export default {
    components: {
        Modal,
    },
    data() {
        return {
            email: '',
            password: '',
            isModalOpen: false,
        };
    },
    methods: {
        handleLogin() {
            console.log('Login logic here');
        },
        showPopUp() {
            this.isModalOpen = true;
        },
        closeModal() {
            this.isModalOpen = false;
        },
    },
};
</script>