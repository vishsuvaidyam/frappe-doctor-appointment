<template>
  <div class="h-screen flex items-center justify-center">
    <div class="max-w-lg bg-white border rounded-lg shadow-md p-6">
      <h2 class="text-xl font-semibold mb-2">Choose Payment Method</h2>
      <p class="text-sm text-gray-600 mb-4">Payment & Billing details such as your balance, channels, & history.</p>

      <form>
        <div class="space-y-4">
          <!-- PayPal -->
          <label class="flex items-center justify-between border rounded-lg p-4 cursor-pointer hover:shadow-sm "
            onclick="window.location.href='/payment';">
            <div class="flex items-center">
              <input type="radio" name="payment-method" class="form-radio text-blue-600" />
              <span class="ml-4 font-medium">Paypal</span>
            </div>
            <img src="https://www.paypalobjects.com/images/shared/paypal-logo-129x32.svg" alt="Paypal" class="h-8" />
          </label>

          <!-- Credit Card -->
          <label class="flex items-center justify-between border rounded-lg p-4 cursor-pointer hover:shadow-sm"
            onclick="window.location.href='/payment';">
            <div class="flex items-center">
              <input type="radio" name="payment-method" class="form-radio text-blue-600" />
              <span class="ml-4 font-medium">Credit Card</span>
            </div>
            <div class="flex space-x-2">
              <!-- <img src="../assets/download (2) 1.png" alt="RuPay" class="w-6 h-6" /> -->
              <img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Visa_Logo.png" alt="Visa"
                class="w-20 h-8" />
            </div>

          </label>

          <!-- UPI -->
          <label class="flex items-center justify-between border rounded-lg p-4 cursor-pointer hover:shadow-sm">
            <div class="flex items-center">
              <input type="radio" name="payment-method" class="form-radio text-blue-600" />
              <span class="ml-4 font-medium">UPI</span>
            </div>
            <img src="../assets/images 1.png" alt="UPI" class="h-8" />
          </label>

          <!-- Radio Button Label -->
          <label class="flex items-center justify-between border rounded-lg p-4 cursor-pointer hover:shadow-sm"
            @click="toggleBankList">
            <div class="flex items-center">
              <input type="checkbox" name="payment-method" class="form-checkbox text-blue-600" @click.stop />
              <span class="ml-4 font-medium">Net Banking</span>
            </div>
            <img src="../assets/download (3) 1.png" alt="Net Banking" class="h-8" />
          </label>

          <!-- Bank List -->
          <div v-show="isBankListVisible" class="w-full max-w-md bg-white shadow-md rounded-lg p-4 mt-4">
            <ul class="space-y-2">
              <!-- State Bank of India -->
              <li class="flex items-center p-3 bg-gray-50 rounded-lg shadow-sm">
                <img src="../assets/SBI.png" alt="SBI" class="w-6 h-6 mr-3">
                <span class="text-gray-700">State Bank of India</span>
              </li>

              <!-- HDFC Bank -->
              <li class="flex items-center p-3 bg-gray-50 rounded-lg shadow-sm">
                <img src="../assets/HDFC.png" alt="HDFC" class="w-6 h-6 mr-3">
                <span class="text-gray-700">HDFC Bank</span>
              </li>

              <!-- ICICI Bank -->
              <li class="flex items-center p-3 bg-gray-50 rounded-lg shadow-sm">
                <img src="../assets/ICIC.png" alt="ICICI" class="w-6 h-6 mr-3">
                <span class="text-gray-700">ICICI Bank</span>
              </li>

              <!-- Axis Bank -->
              <li class="flex items-center p-3 bg-gray-50 rounded-lg shadow-sm">
                <img src="../assets/Axis.png" alt="Axis" class="w-6 h-6 mr-3">
                <span class="text-gray-700">Axis Bank</span>
              </li>

              <!-- Select from all other banks -->
              <li class="flex items-center justify-between p-3 bg-gray-50 rounded-lg shadow-sm">
                <span class="text-gray-700">Select from all other banks</span>
                <svg class="w-5 h-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </li>
            </ul>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const isBankListVisible = ref(false);

function toggleBankList() {
  isBankListVisible.value = !isBankListVisible.value;
}
</script>