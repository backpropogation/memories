<template>
<b-container>
  <b-container class="bv-example-row">
    <b-row>
      <b-col offset="9">
        <router-link to="memory/new" replace>
          <b-button class="mt-2" variant="primary">New memory</b-button>
        </router-link>
      </b-col>
    </b-row>
  </b-container>
  <b-container class="bv-example-row">
    <b-row>
      <b-col>
        <b-card-group deck v-for="memory in memories" :key="memory.title" :memory="memory">
          <b-col class="align-items-center" cols="10" offset="1">
            <b-card
              v-bind:title="memory.title"
              img-alt="Image"
              img-top
              tag="article"
              class="mb-2"
              style="margin-top: 20px"

            >
              <p>{{memory.posted_at}}</p>
              <b-row align-h="center">
                <yandex-map
                  :coords="[memory.latitude, memory.longitude]"
                  style="width: 500px; height: 500px; padding-left: 10px; padding-right: 10px;"
                  zoom="15"
                >
                  <ymap-marker
                    :coords="[memory.latitude, memory.longitude]"
                    marker-id="123"
                    hint-content="some hint"
                  >
                  </ymap-marker>
                </yandex-map>
              </b-row>
              <b-card-text class="mt-5">
                {{memory.description}}
              </b-card-text>

            </b-card>
          </b-col>
          <b-col></b-col>
        </b-card-group>
      </b-col>

    </b-row>
  </b-container>
</b-container>

</template>

<script>
    import axios from 'axios';

    export default {
        name: "memories-list",
        data() {
            return {
                memories: []
            }
        },
        created() {
            const path = 'https://barakhtaev.engineer/api/memories/';
            const headers = {headers: {Authorization: `Token ${localStorage.token}`}}
            axios.get(
                path,
                headers
            ).then((res) => {
                this.memories = res.data;

            })
                .catch((error) => {
                    // eslint-выключение следующей строки
                    console.error(error);
                })
        },

    }
</script>

<style>

</style>
