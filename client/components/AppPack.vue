<template>
  <VContainer
    class="packs"
    id="price"
  >
    <VRow class="section-title mb-15 mt-16 d-flex justify-md-start justify-center text-center">
      <h1>Выберите нужный пакет</h1>
    </VRow>
    <VRow class="packs-body d-flex justify-lg-space-between justify-center align-center mb-16">
      <VCard
        title="– PRO –"
        width="360px"
        height="460px"
        class="packs-body__card d-flex flex-column justify-end"
      >
        <h2 class="packs-body__head mb-5 mt-15">20.000 ₽</h2>
        <p>УМК по робототетхнике <br> и программированию</p>
        <a
          href="#feedback"
          class="packs-body__button mx-auto mb-10 mt-10"
        >Оставить заявку</a>
      </VCard>
      <VCard
        title="– ROBO –"
        width="360px"
        height="460px"
        class="packs-body__card d-flex flex-column justify-end"
      >
        <h2 class="packs-body__head mb-5 mt-15">15.000 ₽</h2>
        <p>УМК по робототехнике </p>
        <a
          href="#feedback"
          class="packs-body__button mx-auto mb-10 mt-16"
        >Оставить заявку</a>
      </VCard>
      <VCard
        title="– PROG –"
        width="360px"
        height="460px"
        class="packs-body__card d-flex flex-column justify-end"
      >
        <h2 class="packs-body__head mb-5 mt-15">10.000 ₽</h2>
        <p>УМК по программированию</p>
        <a
          href="#feedback"
          class="packs-body__button mx-auto mb-10 mt-16"
        >Оставить заявку</a>
      </VCard>
    </VRow>
  </VContainer>
</template>

<script setup lang="ts">

</script>