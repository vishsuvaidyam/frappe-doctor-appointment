<!-- <template>
  <div class="max-w-4xl mx-auto p-6">
    
    <div class="bg-white shadow-lg rounded-lg overflow-hidden">
     
      <div class="relative bg-blue-500 p-6 text-white">
        <div class="flex justify-center items-center">
          <img
            class="w-24 h-24 rounded-full border-4 border-white -mt-2"
            :src="user.profileImage"
            :alt="user.name"
          />
        </div>
        <div class="mt-4 text-center">
          <h2 class="text-xl font-semibold">{{ user.name }}</h2>
          <p class="text-sm">{{ user.status }}</p>
        </div>
      </div>

      
      <div class="p-6 space-y-4">
        <div>
          <h3 class="font-semibold text-gray-700">About</h3>
          <p class="text-gray-600">{{ user.bio }}</p>
        </div>

        <div>
          <h3 class="font-semibold text-gray-700">Contact Information</h3>
          <p class="text-gray-600">
            <strong>Email: </strong>{{ user.email }}
          </p>
          <p class="text-gray-600">
            <strong>Phone: </strong>{{ user.phone }}
          </p>
        </div>

        <div>
          <h3 class="font-semibold text-gray-700">Location</h3>
          <p class="text-gray-600">{{ user.location }}</p>
        </div>
      </div>

      
      <div class="bg-gray-100 p-4 text-center">
        <button class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition">
          Edit Profile
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>

const user = {
  name: 'Vivek Kumar',
  status: 'Available',
  profileImage: 'https://via.placeholder.com/150',
  bio: 'A passionate developer with a love for technology and coding.',
  email: 'vivek@123gmail.com',
  phone: '+91 9876543212',
  location: 'Chhapra,Saran Bihar',
};
</script>

<style scoped>
</style> -->


<!-- <template>
  <div class="w- full h-screen">
    <div class="bg-white h-auto w-200 shadow-md rounded-lg p-6">
      <div class="text-sm text-gray-500 mb-4">
        <a href="#" class="hover:underline">People</a> / <span>Vishwajeet Kumar</span>
      </div>

      <div class="flex items-center space-x-4 mb-6">
        <div class="w-16 h-16 bg-gray-300 rounded-full overflow-hidden">
          <img src="https://via.placeholder.com/150" alt="Profile" class="w-full h-full object-cover">
        </div>
        <h1 class="text-2xl font-bold text-gray-800">Vishwajeet Kumar</h1>
      </div>
      <div class="flex space-x-4 border-b mb-4">
        <button class="pb-2 border-b-2 border-gray-800 text-gray-800 font-medium">About</button>
        <button class="pb-2 text-gray-500 hover:text-gray-800">Certificates</button>
      </div>
      <div class="text-gray-500">
        <h2 class="text-lg font-semibold">Certificates</h2>
        <p>No certificates available.</p>
      </div>
      <div class="mt-6 text-right">
        <button class="px-4 py-2 bg-gray-800 text-white rounded hover:bg-gray-700">Edit Profile</button>
      </div>
    </div>
  </div>

</template> -->

<template>

  <div class="bg-gray-100 h-screen">
    <div class="text-sm text-gray-500 mb-4">
      <a href="#" class="hover:underline">People</a> / <span>Vivek Kumar</span>
    </div>
    <div class="bg-gray-200 h-40"></div>
    <div class="flex flex-col items-center -mt-20">
      <div
        class="w-24 h-24 rounded-full bg-gray-300 flex items-center justify-center text-2xl font-bold text-gray-600 border-4 border-white mt-16 mr-80">
        VK
      </div>
      <h1 class="mt-4 text-lg font-bold text-gray-800">Vivek Kumar</h1>
      <button class="mt-3 px-4 py-2 text-sm bg-blue-500 text-white rounded-md hover:bg-blue-600">
        Edit Profile
      </button>
    </div>
  </div>

</template>