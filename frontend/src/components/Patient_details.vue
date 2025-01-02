<template>
    <div class="max-w-3xl mx-auto p-6 bg-white shadow-md rounded-lg">
        <h2 class="text-2xl font-bold mb-4 text-gray-800">Patient Form</h2>
        <form class="space-y-6">
            <div>
                <h3 class="text-lg font-semibold text-gray-700">Basic Information</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
                    <div>
                        <label class="block text-sm font-medium text-gray-600">Patient Name</label>
                        <input type="text"
                            class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200"
                            placeholder="Enter Your Patient Name ">
                    </div>
                    <div>
                        <label class="block text-sm font-medium ">Gender</label>
                        <select
                            class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200">
                            <option>Male</option>
                            <option>Female</option>
                            <option>Other</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-600">Age</label>
                        <input type="text"
                            class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-600">Contact Number</label>
                        <input type="tel"
                            class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200"
                            placeholder="+1234567890">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-600">Email</label>
                        <input type="Email"
                            class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200"
                            placeholder="Enter Your Email">
                    </div>
                    <div class="">
                        <label class="block text-sm font-medium text-gray-600">Email</label>
                        <input type="Email"
                            class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200"
                            placeholder="Enter Your Email">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-600">Address</label>
                        <textarea
                            class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200"
                            placeholder="Enter Your Address" rows="4"></textarea>
                    </div>
                </div>
            </div>
        </form>
        </div>

</template>