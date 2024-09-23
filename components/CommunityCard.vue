<script setup lang="ts">

const props = defineProps({
  community: { type: Object, required: true },
})

</script>

<template>
  <UCard :ui="{ background: 'bg-gray-100', shadow: false, ring: 'ring-0' }">
    <template #header>
      <h3><ULink class="block" :to="`/communities/${community.slug}`">{{ community.name }}</ULink></h3>
    </template>
  </UCard>
</template>