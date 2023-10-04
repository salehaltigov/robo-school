<template>
  <VContainer
    class="about-school"
    id="about-school"
  >
    <VRow class="about-school__head pt-16 pb-15">
      <h2><b>Robo School</b> – учреждение для формирования кадрового
        <br> педагогического резерва в сфере робототехники
        <br> и программирования
      </h2>
    </VRow>
    <VRow class="about-school__body mb-15">
      <VCol>
        <h1>10</h1>
        <p>УМК по различным направлениям по робототехнике</p>
      </VCol>
      <VCol>
        <h1>20</h1>
        <p>Школ, в которых запущена робототехника</p>
      </VCol>
      <VCol>
        <h1>100</h1>
        <p>Педагогов прошедших курсы повышения квалификации</p>
      </VCol>
      <VCol>
        <h1>10 000</h1>
        <p>Обученных детей на базе собственных центров</p>
      </VCol>
    </VRow>
  </VContainer>
  <VContainer class="mt-15">
    <VRow class="about-course__head mb-15">
      <h1>Что вы получите после курса</h1>
    </VRow>
    <VRow class="about-course__body">
      <VCol>
        <h2>Удостоверение</h2>
        <p>Дающее право преподавать робототехнику для детей 6-12 лет в образовательных учреждениях</p>
      </VCol>
      <VCol>
        <h2>Знания</h2>
        <p>По основам разработки учебно-методических комплексов по робототехнике и программированию</p>
      </VCol>
      <VCol>
        <h2>Практику
          <VTooltip text="При наличии свободных мест">
            <template v-slot:activator="{ props }">
              <VIcon
                size="small"
                color="#141024"
                icon="mdi-information-outline"
                v-bind="props"
              >
              </VIcon>
            </template>
          </VTooltip>
        </h2>
        <p>Возможность пройти практику по преподаванию робототехники на базе R:ED LAB (в оффлайн или онлайн формате)</p>
      </VCol>
    </VRow>
  </VContainer>
</template>

<script setup lang="ts">
</script>