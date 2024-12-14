<template>
    <div class="flex gap-2 items-center">
        <button @click="openDialog('Register')"
            class="w-[74px] h-10 text-h5 rounded-md">Register</button>
        <button @click="openDialog('Login')"
            class="w-[74px] h-10 text-h5 rounded-md bg-secondary text-white">Login</button>
    </div>
    <TransitionRoot as="template" :show="store.authPopup">
        <Dialog class="relative z-20">
            <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
                leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
                <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
            </TransitionChild>

            <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
                <div class="flex min-h-full justify-center p-4 text-center items-center sm:p-0">
                    <TransitionChild as="template" enter="ease-out duration-300"
                        enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                        enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
                        leave-from="opacity-100 translate-y-0 sm:scale-100"
                        leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
                        <DialogPanel
                            class="relative  transform overflow-hidden  bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-2xl">
                         <X @click="store.authPopup= false" class="text-sm  cursor-pointer absolute right-1 -top-1 mt-2" />
                            <Register v-if="store.auth" />
                            <Login v-if="!store.auth" />
                        </DialogPanel>
                    </TransitionChild>
                </div>
            </div>
        </Dialog>
    </TransitionRoot>
</template>

<script setup>
import { inject, ref, watch } from 'vue'
import { Dialog, DialogPanel, TransitionChild, TransitionRoot } from '@headlessui/vue'
import Login from './Login.vue';
import Register from './Register.vue';
import { X } from 'lucide-vue-next';

const store = inject('store');

watch(()=> store.authPopup, (value) => {
    if (!value) {
        store.save_as_login = false;
        setTimeout(() => {
            store.isForgetPas = false;
        }, 300)
    }
})
watch(()=> store.save_as_login, (value) => {
    if (value) {
        openDialog('Login');
    }
})
const openDialog = (el) => {
    store.authPopup = true;
    if (el === 'Register') {
        store.auth = true;
    } else {
        store.auth = false;
    }
}
</script>