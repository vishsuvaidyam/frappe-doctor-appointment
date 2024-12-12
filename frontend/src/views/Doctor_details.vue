<template>
    <div class="w-full  px-20 ">
        <div class="flex gap-10 w-full h-auto">
            <div class="w-1/6  ">
                <div class="border rounded-lg bg-blue-600">
                    <img class="h-64 flex justify-center" src="../assets/doc13.png" />
                </div>
            </div>
            <div class="w-4/5 border border-gray-300 rounded-lg">
                <div class=" px-8 py-8 ">
                    <h1 class="text-3xl text-gray-700 font-bold py-1 flex items-center gap-2 "> Dr. Chloe Evans 
                        <img class="w-4 h-4" src="../assets/download (1).svg" alt="" srcset=""></h1>
                    <p class="text-md text-gray-700 font-normal py-1">MBBS - General physician <span class="border px-4 py-1 rounded-3xl">2 Year</span></p>
                    <p class="flex gap-2 items-center text-md font-semibold py-2">About
                        <span class="">
                            <img src="../assets/download.svg" alt="" srcset="">
                        </span>
                    </p>
                    <div class="w-3/5">
                        <p class="text-sm font-normal text-gray-600 ">Dr. Davis has a strong commitment to delivering comprehensive medical care, focusing on
                        preventive medicine, early diagnosis, and effective treatment strategies. Dr. Davis has a strong
                        commitment to delivering comprehensive medical care, focusing on preventive medicine, early
                        diagnosis, and effective treatment strategies.
                    </p>
                    </div>
                    <p class="text-md font-semibold pt-4 text-gray-500">Apointment fee:<span class="text-md font-semibold px-2 text-gray-800">$30</span></p>
                </div>
            </div>
        </div>
        <div class="flex gap-10 w-full h-64 pt-8">
            <div class="w-1/6  ">
            </div>
            <div class="w-4/5">
                <h1>Booking slots</h1>
                <div class="pt-4 flex gap-4">
                    <button class="px-2 text-sm font-normal py-10 border rounded-full">THU 12</button>
                    <button class="px-2 text-sm font-normal py-10 border rounded-full">THU 12</button>
                    <button class="px-2 text-sm font-normal py-10 border rounded-full">THU 12</button>
                    <button class="px-2 text-sm font-normal py-10 border rounded-full">THU 12</button>
                    <button class="px-2 text-sm font-normal py-10 border rounded-full">THU 12</button>
                    <button class="px-2 text-sm font-normal py-10 border rounded-full">THU 12</button>
                    <button class="px-2 text-sm font-normal py-10 border rounded-full">THU 12</button>
                </div>
                <div class="flex gap-4 pt-4">
                    <button class="px-8 py-2 border rounded-full">10:30 am</button>
                    <button class="px-8 py-2 border rounded-full">10:30 am</button>
                    <button class="px-8 py-2 border rounded-full">10:30 am</button>
                    <button class="px-8 py-2 border rounded-full">10:30 am</button>
                    <button class="px-8 py-2 border rounded-full">10:30 am</button>
                    <button class="px-8 py-2 border rounded-full">10:30 am</button>
                </div>
                <button class="px-10 py-2 border rounded-3xl mt-4 bg-blue-600 text-white text-sm font-normal">Book an
                    appointment</button>
            </div>
        </div>
        <div class="pt-10">
            <Realated_doctors />
        </div>
    </div>
</template>
<script setup>
import Realated_doctors from './Realated_doctors.vue';
</script>