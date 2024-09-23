<script setup lang="ts">

const props = defineProps({
  user: { type: Object, required: true },
})

</script>
<template>
  <UButton color="gray" variant="link" :padded="false" size="2xs">
    <template #leading>
      <UAvatar :src="user.picture" size="3xs" />
    </template>
    {{ user.name }}
  </UButton>
</template>