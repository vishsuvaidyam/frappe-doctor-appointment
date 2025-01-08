<template>
  <div class="max-w-md mx-auto p-6 bg-white shadow-lg rounded-lg mt-10">
    <h2 class="text-2xl font-semibold mb-6 text-gray-800">Payment</h2>

    <!-- Card Display -->
    <div class="flex items-center justify-center mb-6">
      <div class="w-80 h-auto bg-orange-400 rounded-lg p-4 shadow-md text-white">
        <div class="text-sm mb-4">CARD</div>
        <div class="text-lg font-bold tracking-widest mb-4">XXXX XXXX XXXX XXXX {{card1}} {{card2}} {{card3}} {{card4}}</div>
        <div class="flex justify-between text-sm">
          <div>
            <div class="uppercase text-xs">Card Holder</div>
            <div class="text-base font-medium">N° carte bancaire</div>
          </div>
          <div>
            <div class="uppercase text-xs">Expiry</div>
            <div class="text-base font-medium">XX/XX</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Payment Form -->
    <form>
      <!-- Cardholder Name -->
      <div class="mb-4">
        <label class="block text-gray-700 font-medium mb-2">Cardholder Name</label>
        <input v-model="Cardholder" type="text" placeholder="Enter Name"
          class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-orange-300" />
      </div>

      <!-- Card Number -->
      <div class="mb-4">
        <label class="block text-gray-700 font-medium mb-2">Card Number</label>
        <div class="flex gap-2">
          <input v-model="card1" type="text" maxlength="4" placeholder="XXXX"
            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-orange-300" />
          <input v-model="card2" type="text" maxlength="4" placeholder="XXXX"
            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-orange-300" />
          <input v-model="card3" type="text" maxlength="4" placeholder="XXXX"
            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-orange-300" />
          <input v-model="card4" type="text" maxlength="4" placeholder="XXXX"
            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-orange-300" />
        </div>
      </div>

      <!-- Expiry Date -->
      <div class="mb-4">
        <label class="block text-gray-700 font-medium mb-2">Expiry Date</label>
        <div class="flex gap-2">
          <input type="text" placeholder="MM"
            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-orange-300" />
          <input type="text" placeholder="YY"
            class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-orange-300" />
        </div>
      </div>

      <!-- CVV -->
      <div class="mb-6">
        <label class="block text-gray-700 font-medium mb-2">CVV / CVC</label>
        <input type="text" maxlength="3" placeholder="123"
          class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-orange-300" />
      </div>

      <!-- Pay Now Button -->
      <button type="submit"
        class="w-full bg-blue-600 text-white py-2 rounded-lg shadow-md hover:bg-blue-600 transition">
        Pay Now
      </button>
    </form>
  </div>

</template>

<script setup>

import { ref } from 'vue';

  const Cardholder=ref();
  const card1=ref();
  const card2=ref();
  const card3=ref();
  const card4=ref();
</script>