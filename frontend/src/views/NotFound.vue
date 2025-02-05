<template>
    <div class="fixed inset-0 opacity-100 bg-gray-50 flex items-center justify-center px-4">
        <div class="w-full flex flex-col gap-3 justify-center items-center ">
            <p class="text-4xl text-gray-600 ">Page Not Found</p>
            <button class="rounded-md text-base flex items-center gap-2" @click="router.back(-1)"><MoveLeft/> Back to previous route</button>
        </div>
    </div>
</template>

<script setup>
import {MoveLeft} from 'lucide-vue-next'
import { useRouter } from 'vue-router'
const router = useRouter()
</script>