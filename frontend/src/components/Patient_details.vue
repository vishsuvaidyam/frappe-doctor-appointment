<!-- <template>
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
                        <label class="block text-sm font-medium text-gray-700">Gender</label>
                        <select
                            class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200 bg-white text-gray-900">
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
                            placeholder="+911234567890">
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
                <div class="mt-8 flex justify-center">
                    <button type="submit"
                        class="w-80 px-4 py-2 text-white bg-indigo-600 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500">
                        Submit
                    </button>
                </div>
            </div>
        </form>
    </div>

</template> -->
<template>
    <div class="max-w-lg mx-auto mt-10 p-6 bg-white shadow-md rounded-md">
        <h2 class="text-2xl font-bold text-gray-700 mb-4">Book an Appointment</h2>
        <form class="space-y-4">
            <!-- Patient Name -->
            <div>
                <label class="block text-sm font-medium text-gray-600">Patient Name</label>
                <input type="text" placeholder="Enter Full Name"
                    class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200" required>
            </div>

            <!-- Contact Number -->
            <div>
                <label class="block text-sm font-medium text-gray-600">Contact Number</label>
                <input type="tel" placeholder="Enter Contact Number"
                    class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200" required>
            </div>

            <!-- Email Address -->
            <div>
                <label class="block text-sm font-medium text-gray-600">Email Address</label>
                <input type="email" placeholder="Enter Email Address"
                    class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200" required>
            </div>

            <!-- Appointment Date -->
            <div>
                <label class="block text-sm font-medium text-gray-600">Appointment Date</label>
                <input type="date"
                    class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200" required>
            </div>

            <!-- Appointment Time -->
            <div>
                <label class="block text-sm font-medium text-gray-600">Appointment Time</label>
                <input type="time"
                    class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200" required>
            </div>

            <!-- Doctor Selection -->
            <div>
                <label class="block text-sm font-medium text-gray-600">Select Doctor</label>
                <select
                    class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200 bg-gray-50 text-gray-700"
                    required>
                    <option value="">Select a Doctor</option>
                    <option>Dr. Timothy White</option>
                    <option>Dr. Ava Mitchell</option>
                    <option>Dr. Christopher Lee</option>
                    <option>Dr. Jennifer Garcia</option>
                    <option>Dr. Emily Larson</option>
                    <option>Dr. Sarah Patel James</option>
                </select>
            </div>


            <div>
                <label class="block text-sm font-medium text-gray-600">Additional Notes (Optional)</label>
                <textarea placeholder="Add any special requests or notes"
                    class="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-indigo-200"
                    rows="3"></textarea>
            </div>

            <div class="flex justify-center">
                <button type="submit"
                    class="px-6 py-2 text-white bg-indigo-600 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring focus:ring-indigo-500">
                    Book Appointment
                </button>
            </div>
        </form>
    </div>

</template>