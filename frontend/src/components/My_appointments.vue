<template>
    <div class="mx-auto mt-4">
        <h2 class="text-xl font-semibold mb-2">My appointments</h2>
        <div class="flex items-start p-4 border rounded-lg shadow-sm">
            <img class="w-36 h-30 object-cover rounded-md border" src="../assets/doc9.png" alt="Doctor" />

            <div class="flex-1 ml-6">
                <h3 class="text-lg font-bold">Dr. Emily Larson</h3>
                <p class="text-sm text-gray-600">Gynecologist</p>
                <p class="text-sm text-gray-600">
                    <span class="font-semibold">Address: <br> </span> 27th Cross, Richmond  <br> Circle, Ring Road, London
                </p>
                <p class="text-sm text-gray-600">
                    <span class="font-semibold">Date & Time:</span> 27 December 2024 | 10:30 AM
                </p>
            </div>

            <div class="flex flex-col space-y-3 py-8">
                <button class="bg-gray-100 text-black text-sm py-2 px-4 rounded-lg hover:bg-blue-600  hover:text-white"
                    @click="payOnline">
                    Pay Online
                </button>
                <button class="bg-gray-100 text-sm py-2 px-4 rounded-lg hover:bg-red-500 hover:text-white"
                    @click="cancelAppointment">
                    Cancel Appointment
                </button>

            </div>
        </div>
    </div>
</template>

<script setup>

</script>