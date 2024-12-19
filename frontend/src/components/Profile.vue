<template>
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
</style>
