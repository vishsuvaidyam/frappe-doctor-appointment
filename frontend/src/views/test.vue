<template>
    <div>
      <div v-if="dateRange">
        <p><strong>Start Date:</strong> {{ formattedStartDate }}</p>
        <p><strong>End Date:</strong> {{ formattedEndDate }}</p>
        <p><strong>Date Range:</strong> {{ dateRange }}</p>
      </div>
      <div v-else>
        <p>Loading date range...</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  
  // States to hold start date, end date, and formatted date range
  const dateRange = ref('');
  const formattedStartDate = ref('');
  const formattedEndDate = ref('');
  
  // Fetch date range data from the backend API
  const fetchDateRange = async () => {
    try {
      // Adjust this URL if needed, to point to the correct API endpoint
      const response = await axios.get('/api/method/appointments_management.controllers.api.get_date_range');
      const data = response.data;  // Directly access the response data
      
      console.log(data);  // Check the response structure in the console
  
      // Ensure the data is valid before accessing fields
      if (data && data.data && data.data.length > 0) {
        const { start_date, end_date } = data.data[0];
  
        // Format the dates
        formattedStartDate.value = formatDate(start_date);
        formattedEndDate.value = formatDate(end_date);
  
        // Combine formatted dates into a range string
        dateRange.value = `${formattedStartDate.value} - ${formattedEndDate.value}`;
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };
  
  // Helper function to format date to a readable string
  const formatDate = (dateString) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString();  // Adjust the date format if needed
  };
  
  // Fetch data when the component is mounted
  onMounted(() => {
    fetchDateRange();
  });
  </script>
  
  <style scoped>
  /* Add any styles you need here */
  </style>
  