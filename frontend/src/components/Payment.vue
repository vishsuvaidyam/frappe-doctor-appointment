<template>
  <div class="bg-gray-50 w-full max-h-full p-10 inset-0">
    <div
      class="max-w-md mx-auto p-6 px-10 bg-opacity-50 rounded-md bg-gradient-to-t from-gray-100 border to-white mt-10">
      <h2 class="text-2xl font-semibold font-serif mb-4 text-gray-800">Payment</h2>

      <!-- Card Display with Flip Animation -->
      <div class="relative w-80 h-44 mx-auto mb-6 perspective">
        <!-- Card Front -->
        <div
          class="absolute w-full rounded-md h-full bg-yellow-400 text-black transform transition-transform duration-500"
          :class="{ 'rotate-y-180': showBack }">
          <div class="p-4" :class="{ hidden: showBack }">
            <div class="text-sm mb-4">CARD</div>
            <div class="text-lg font-bold tracking-widest mb-4">
              {{ displayCardNumber }}
            </div>
            <div class="flex justify-between text-sm">
              <div>
                <div class="uppercase text-xs">Card Holder</div>
                <div class="text-base font-medium">
                  {{ Cardholder || "John Doe" }}
                </div>
              </div>
              <div>
                <div class="uppercase text-xs">Expiry</div>
                <div class="text-base font-medium">
                  {{ validCardNumber }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Card Back -->
        <div class="absolute w-full h-full bg-transparent z-50 text-white transition-transform duration-500"
          :class="{ hidden: !showBack, 'rotate-y-0': !showBack }">
          <div class="p-4" :class="{ 'delay-300': !showBack }">
            <div class="text-sm text-gray-400 mb-4">CVV</div>
            <div class="flex justify-start">
              <div
                class="w-32 h-10 bg-gray-600 rounded text-center text-lg font-bold tracking-widest text-white flex items-center justify-center">
                {{ cvv || "***" }}
              </div>
            </div>
          </div>
        </div>
      </div>

      <form @submit.prevent="validateForm">
        <!-- Cardholder Name -->
        <div class="mb-4">
          <label class="block text-gray-700 font-medium text-sm mb-2">Cardholder Name</label>
          <input v-model="Cardholder" type="text" placeholder="Enter Name"
            class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring focus:ring-orange-300" />
          <p v-if="errors.cardholder" class="text-red-500 text-sm mt-1">{{ errors.cardholder }}</p>
        </div>

        <!-- Card Number -->
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-medium mb-2">Card Number</label>
          <div class="flex gap-2">
            <input v-model="card1" type="text" maxlength="4" placeholder="XXXX"
              class="w-full px-4 py-1 border focus:outline-none focus:ring outline-none" />
            <input v-model="card2" type="text" maxlength="4" placeholder="XXXX"
              class="w-full px-4 py-1 border focus:outline-none focus:ring focus:ring-orange-300" />
            <input v-model="card3" type="text" maxlength="4" placeholder="XXXX"
              class="w-full px-4 py-1 border focus:outline-none focus:ring focus:ring-orange-300" />
            <input v-model="card4" type="text" maxlength="4" placeholder="XXXX"
              class="w-full px-4 py-1 border focus:outline-none focus:ring focus:ring-orange-300" />
          </div>
          <p v-if="errors.cardNumber" class="text-red-500 text-sm mt-1">{{ errors.cardNumber }}</p>
        </div>

        <!-- Expiry Date -->
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-medium mb-2">Expiry Date</label>
          <div class="flex gap-2">
            <input v-model="month" type="text" maxlength="2" placeholder="MM"
              class="w-full px-4 py-1 border focus:outline-none focus:ring focus:ring-orange-300" />
            <input v-model="year" type="text" maxlength="2" placeholder="YY"
              class="w-full px-4 py-1 border focus:outline-none focus:ring focus:ring-orange-300" />
          </div>
          <p v-if="errors.expiryDate" class="text-red-500 text-sm mt-1">{{ errors.expiryDate }}</p>
        </div>

        <!-- CVV -->
        <div class="mb-6">
          <label class="block text-gray-700 font-medium text-sm mb-2">CVV / CVC</label>
          <input v-model="cvv" @focus="flipToBack" @blur="flipToFront" type="text" maxlength="3" placeholder="123"
            class="w-full px-4 py-2 delay-300 border focus:outline-none focus:ring focus:ring-orange-300" />
          <p v-if="errors.cvv" class="text-red-500 text-sm mt-1">{{ errors.cvv }}</p>
        </div>

        <!-- Pay Now Button -->
        <button type="submit"
          class="px-10 bg-sky-600 rounded text-white py-2 shadow-md hover:bg-blue-500 active:bg-blue-700 transition">
          Pay Now
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

// Reactive states
const Cardholder = ref("");
const card1 = ref("");
const card2 = ref("");
const card3 = ref("");
const card4 = ref("");
const month = ref("");
const year = ref("");
const cvv = ref("");
const showBack = ref(false);
const errors = ref({});

// Computed properties
const displayCardNumber = computed(() => {
  const parts = [card1.value, card2.value, card3.value, card4.value];
  return parts.every((part) => part === "")
    ? "XXXX XXXX XXXX XXXX"
    : parts.join(" ");
});

const validCardNumber = computed(() => {
  return month.value && year.value ? `${month.value}/${year.value}` : "MM / YY";
});

// Methods to handle card flip
const flipToBack = () => {
  showBack.value = true;
};

const flipToFront = () => {
  showBack.value = false;
};

// Form validation
const validateForm = () => {
  errors.value = {};

  // Validate cardholder name
  if (!Cardholder.value.trim()) {
    errors.value.cardholder = "Cardholder name is required.";
  } else if (!/^[a-zA-Z\s]+$/.test(Cardholder.value)) {
    errors.value.cardholder = "Cardholder name can only contain letters.";
  }

  // Validate card number
  const cardParts = [card1.value, card2.value, card3.value, card4.value];
  if (cardParts.some((part) => part.length < 4)) {
    errors.value.cardNumber = "Card number must be 16 digits.";
  }

  // Validate expiry date
  const monthNum = parseInt(month.value, 10);
  const yearNum = parseInt(year.value, 10);
  if (!month.value || !year.value || monthNum < 1 || monthNum > 12 || yearNum < 0) {
    errors.value.expiryDate = "Invalid expiry date.";
  }

  // Validate CVV
  if (!cvv.value || cvv.value.length !== 3 || !/^\d{3}$/.test(cvv.value)) {
    errors.value.cvv = "Invalid CVV.";
  }

  if (Object.keys(errors.value).length === 0) {
    alert("Payment successful!");
  }
};

</script>

<style>
/* Perspective and Flip Animation */
.perspective {
  perspective: 1000px;
}

.rotate-y-0 {
  transform: rotateY(0deg);
}

.rotate-y-180 {
  transform: rotateY(180deg);
}
</style>
