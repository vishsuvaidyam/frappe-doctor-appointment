<template>
    <div class="max-w-lg mx-auto bg-white border rounded-lg shadow-md p-6">
  <h2 class="text-xl font-semibold mb-2">Choose Payment Method</h2>
  <p class="text-sm text-gray-600 mb-4">Payment & Billing details such as your balance, channels, & history.</p>
  
  <form>
    <div class="space-y-4">
      <!-- PayPal -->
      <label class="flex items-center justify-between border rounded-lg p-4 cursor-pointer hover:shadow-sm">
        <div class="flex items-center">
          <input type="radio" name="payment-method" class="form-radio text-blue-600" />
          <span class="ml-4 font-medium">Paypal</span>
        </div>
        <img src="https://www.paypalobjects.com/images/shared/paypal-logo-129x32.svg" alt="Paypal" class="h-8" />
      </label>

      <!-- Credit Card -->
      <label class="flex items-center justify-between border rounded-lg p-4 cursor-pointer hover:shadow-sm">
        <div class="flex items-center">
          <input type="radio" name="payment-method" class="form-radio text-blue-600" />
          <span class="ml-4 font-medium">Credit Card</span>
        </div>
        <div class="flex space-x-2">
          <img src="../assets/download (2) 1.png" alt="RuPay" class="h-8" />
          <img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Visa_Logo.png" alt="Visa" class="h-8" />
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

      <!-- Net Banking -->
      <label class="flex items-center justify-between border rounded-lg p-4 cursor-pointer hover:shadow-sm">
        <div class="flex items-center">
          <input type="radio" name="payment-method" class="form-radio text-blue-600" />
          <span class="ml-4 font-medium">Net Banking</span>
        </div>
        <img src="../assets/download (3) 1.png" alt="Net Banking" class="h-8" />
      </label>
    </div>
  </form>
</div>

</template>