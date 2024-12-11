<template>
  <div class="h-auto w-full">
    <div class="bg-blue-500  h-auto flex items-center rounded-lg">
      <div class="container mx-auto px-6 md:px-12 lg:px-16">
        <div class="flex flex-col lg:flex-row items-center">
          <!-- Left Content -->
          <div class="lg:w-1/2 text-center lg:text-left pb-8 lg:pb-0">
            <h1 class="text-4xl md:text-5xl font-bold text-white pb-4">
              Book Appointment <br />
              With Trusted Doctors
            </h1>

            <div class="flex items-center space-x-4 pb-6">
              <!-- Avatars -->
              <div class="flex -space-x-4 ">
                <img class="w-10 h-10 rounded-full border-2 border-white" src="../assets/logo.jpg" alt="Person 1" />
                <img class="w-10 h-10 rounded-full border-2 border-white" src="../assets/logo.jpg" alt="Person 2" />
                <img class="w-10 h-10 rounded-full border-2 border-white" src="../assets/logo.jpg" alt="Person 3" />
                <p class="text-white text-sm px-12">
                  Simply browse through our extensive list of trusted doctors,
                  schedule your appointment hassle-free.
                </p>
              </div>
            </div>
            <!-- Button -->
            <a href="#"
              class="bg-white text-gray-500  text-sm font-semibold py-3 px-6 rounded-3xl shadow-lg hover:bg-blue-100 transition">
              Book appointment →
            </a>
          </div>

          <!-- Right Content -->
          <div class="lg:w-1/2 flex justify-center">
            <img class="w-full max-w-md lg:max-w-full" src="../assets/header_img-DhAi3lLA.png" alt="Doctors" />
          </div>
        </div>
      </div>
    </div>

    <section class="text-center py-12">
      <h2 class="text-2xl font-bold text-gray-800">Find by Speciality</h2>
      <p class="text-gray-500 mt-2">Simply browse through our extensive list of trusted doctors, schedule your
        appointment hassle-free.</p>

      <div class="mt-8 flex flex-wrap justify-center gap-6">
        <!-- Speciality Cards -->
        <div class="flex flex-col items-center">
          <div class="w-20 h-20 bg-blue-100 rounded-full flex items-center justify-center">
            <img src="../assets/gen_ph.svg" alt="General physician icon">
          </div>
          <p class="mt-2 text-sm text-gray-700">General physician</p>
        </div>
        <div class="flex flex-col items-center">
          <div class="w-20 h-20 bg-blue-100 rounded-full flex items-center justify-center">
            <img src="../assets/Gynecologist-Av1zZu4d.svg" alt="Gynecologist icon">
          </div>
          <p class="mt-2 text-sm text-gray-700">Gynecologist</p>
        </div>
        <div class="flex flex-col items-center">
          <div class="w-20 h-20 bg-blue-100 rounded-full flex items-center justify-center">
            <img src="../assets/dram.svg" alt="Dermatologist icon">
          </div>
          <p class="mt-2 text-sm text-gray-700">Dermatologist</p>
        </div>
        <div class="flex flex-col items-center">
          <div class="w-20 h-20 bg-blue-100 rounded-full flex items-center justify-center">
            <img src="../assets/Pediatricians-C6nmx5n8.svg" alt="Pediatricians icon">
          </div>
          <p class="mt-2 text-sm text-gray-700">Pediatricians</p>
        </div>
        <div class="flex flex-col items-center">
          <div class="w-20 h-20 bg-blue-100 rounded-full flex items-center justify-center">
            <img src="../assets/Neurologist-CuaLxNpX.svg" alt="Neurologist icon">
          </div>
          <p class="mt-2 text-sm text-gray-700">Neurologist</p>
        </div>
        <div class="flex flex-col items-center">
          <div class="w-20 h-20 bg-blue-100 rounded-full flex items-center justify-center">
            <img src="../assets/Gastroenterologist-CTgzRFeY.svg" alt="Gastroenterologist icon">
          </div>
          <p class="mt-2 text-sm text-gray-700">Gastroenterologist</p>
        </div>
      </div>
    </section>

    <!-- Top Doctors Section -->
    <section class="py-12 bg-white">
      <div class="text-center">
        <h2 class="text-2xl font-bold text-gray-800">Top Doctors to Book</h2>
        <p class="text-gray-500 mt-2">Simply browse through our extensive list of trusted doctors.</p>
      </div>

      <div class="mt-8 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-6 px-4 sm:px-8">
        <!-- Doctor Cards -->
        <div class="bg-white shadow-lg rounded-lg p-4 text-center">
          <img class="w-24 h-24 mx-auto rounded-full" src="https://via.placeholder.com/150" alt="Doctor image">
          <div class="mt-4">
            <span class="text-green-500 text-sm font-medium">● Available</span>
            <h3 class="text-lg font-semibold text-gray-800 mt-2">Dr. Richard James</h3>
            <p class="text-sm text-gray-600">General physician</p>
          </div>
        </div>
        <div class="bg-white shadow-lg rounded-lg p-4 text-center">
          <img class="w-24 h-24 mx-auto rounded-full" src="https://via.placeholder.com/150" alt="Doctor image">
          <div class="mt-4">
            <span class="text-green-500 text-sm font-medium">● Available</span>
            <h3 class="text-lg font-semibold text-gray-800 mt-2">Dr. Emily Larson</h3>
            <p class="text-sm text-gray-600">Gynecologist</p>
          </div>
        </div>
        <div class="bg-white shadow-lg rounded-lg p-4 text-center">
          <img class="w-24 h-24 mx-auto rounded-full" src="https://via.placeholder.com/150" alt="Doctor image">
          <div class="mt-4">
            <span class="text-green-500 text-sm font-medium">● Available</span>
            <h3 class="text-lg font-semibold text-gray-800 mt-2">Dr. Sarah Patel</h3>
            <p class="text-sm text-gray-600">Dermatologist</p>
          </div>
        </div>
        <div class="bg-white shadow-lg rounded-lg p-4 text-center">
          <img class="w-24 h-24 mx-auto rounded-full" src="https://via.placeholder.com/150" alt="Doctor image">
          <div class="mt-4">
            <span class="text-green-500 text-sm font-medium">● Available</span>
            <h3 class="text-lg font-semibold text-gray-800 mt-2">Dr. Christopher Lee</h3>
            <p class="text-sm text-gray-600">Pediatricians</p>
          </div>
        </div>
        <div class="bg-white shadow-lg rounded-lg p-4 text-center">
          <img class="w-24 h-24 mx-auto rounded-full" src="https://via.placeholder.com/150" alt="Doctor image">
          <div class="mt-4">
            <span class="text-green-500 text-sm font-medium">● Available</span>
            <h3 class="text-lg font-semibold text-gray-800 mt-2">Dr. Jennifer Garcia</h3>
            <p class="text-sm text-gray-600">Neurologist</p>
          </div>
        </div>
        <div class="bg-white shadow-lg rounded-lg p-4 text-center">
          <img class="w-24 h-24 mx-auto rounded-full" src="https://via.placeholder.com/150" alt="Doctor image">
          <div class="mt-4">
            <span class="text-green-500 text-sm font-medium">● Available</span>
            <h3 class="text-lg font-semibold text-gray-800 mt-2">Dr. Andrew Williams</h3>
            <p class="text-sm text-gray-600">Gastroenterologist</p>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
</script>
