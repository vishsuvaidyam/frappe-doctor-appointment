<template>
    <div class="w-full h-auto">
        <section class="py-12 bg-white">
            <div class="text-center">
                <h2 class="text-2xl font-bold text-gray-800">Top Doctors to Book</h2>
                <p class="text-gray-800 mt-2">Simply browse through our extensive list of trusted doctors.</p>
            </div>

            <div class="mt-8 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-6 px-4 sm:px-8">
                <div class="bg-[#e9efff] shadow-lg rounded-lg border-blue-500 border-t border-b p-4 text-center">
                    <img class="w-24 h-24 mx-auto rounded-full" src="../assets/doc2.png" alt="Doctor image">
                    <div class="mt-4">
                        <span class="text-green-500 text-sm font-medium">● Available</span>
                        <h3 class="text-lg font-semibold text-gray-800 mt-2">Dr. Richard James</h3>
                        <p class="text-sm text-gray-600">General physician</p>
                    </div>
                </div>
                <div class="bg-white shadow-lg rounded-lg border-blue-500 border-t border-b  p-4 text-center">
                    <img class="w-24 h-24 mx-auto rounded-full" src="../assets/doc1.png" alt="Doctor image">
                    <div class="mt-4">
                        <span class="text-green-500 text-sm font-medium">● Available</span>
                        <h3 class="text-lg font-semibold text-gray-800 mt-2">Dr. Emily Larson</h3>
                        <p class="text-sm text-gray-600">Gynecologist</p>
                    </div>
                </div>
                <div class="bg-white shadow-lg rounded-lg border-blue-500 border-t border-b  p-4 text-center">
                    <img class="w-24 h-24 mx-auto rounded-full" src="../assets/doc2.png" alt="Doctor image">
                    <div class="mt-4">
                        <span class="text-green-500 text-sm font-medium">● Available</span>
                        <h3 class="text-lg font-semibold text-gray-800 mt-2">Dr. Sarah Patel</h3>
                        <p class="text-sm text-gray-600">Dermatologist</p>
                    </div>
                </div>
                <div class="bg-white shadow-lg rounded-lg border-blue-500 border-t border-b  p-4 text-center">
                    <img class="w-24 h-24 mx-auto rounded-full" src="../assets/doc3.png" alt="Doctor image">
                    <div class="mt-4">
                        <span class="text-green-500 text-sm font-medium">● Available</span>
                        <h3 class="text-lg font-semibold text-gray-800 mt-2">Dr. Christopher Lee</h3>
                        <p class="text-sm text-gray-600">Pediatricians</p>
                    </div>
                </div>
                <div class="bg-white shadow-lg rounded-lg border-blue-500 border-t border-b  p-4 text-center">
                    <img class="w-24 h-24 mx-auto rounded-full" src="../assets/doc4.png" alt="Doctor image">
                    <div class="mt-4">
                        <span class="text-green-500 text-sm font-medium">● Available</span>
                        <h3 class="text-lg font-semibold text-gray-800 mt-2">Dr. Jennifer Garcia</h3>
                        <p class="text-sm text-gray-600">Neurologist</p>
                    </div>
                </div>
                <div class="bg-white shadow-lg rounded-lg border-blue-500 border-t border-b  p-4 text-center">
                    <img class="w-24 h-24 mx-auto rounded-full" src="../assets/doc1.png" alt="Doctor image">
                    <div class="mt-4">
                        <span class="text-green-500 text-sm font-medium">● Available</span>
                        <h3 class="text-lg font-semibold text-gray-800 mt-2">Dr. Andrew Williams</h3>
                        <p class="text-sm text-gray-600">Gastroenterologist</p>
                    </div>
                </div>
            </div>
            <div class="flex justify-center items-center pt-5">
                <router-link to="/doctors" class=" px-10 py-2 rounded-3xl border">
                    More
                </router-link>
            </div>
        </section>
    </div>
</template>
<script setup>
</script>