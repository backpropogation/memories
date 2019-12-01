<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Your memory:"
        label-for="input-1"
        description="We'll never share your memory with anyone else."
      >
        <b-form-input
          id="input-1"
          v-model="form.title"
          type="text"
          required
          placeholder="Enter title"
        ></b-form-input>
      </b-form-group>
      <b-form-group>
        <b-row align-h="center">
          <yandex-map
            :coords="coords"
            style="width: 500px; height: 500px;"
            @click="onClick"
            zoom="10"
          >
            <ymap-marker
              :coords="coords"
              marker-id="123"
              hint-content="some hint"
            >
            </ymap-marker>
          </yandex-map>
        </b-row>
      </b-form-group>
      <b-form-group id="input-group-2" label="Your comment:" label-for="input-2">
        <b-form-textarea
          id="input-2"
          v-model="form.description"
          required
          placeholder="Enter comment"
        ></b-form-textarea>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>

  </div>

</template>

<script>
    import axios from 'axios';
    const path = 'http://0.0.0.0:8000/api/memories/';
    export default {

        name: 'memory-form',
        data() {
            return {
                form: {
                    title: '',
                    description: '',
                    longitude: 56.026842,
                    latitude: 92.725653,

                },
                coords: [56.026842, 92.725653],
                show: true
            }
        },
        methods: {
            onSubmit(evt) {
                const headers = {headers: {Authorization: `Token ${localStorage.token}`}}
                console.log(this.form)
                axios.post(
                    path,
                    this.form,
                    headers
                ).then((res) => {
                    if (res.status === 201)
                    {
                        this.$router.push('/memories-list')
                    }
                    else {
                        alert('Something went wrong')
                    }
                })
                    .catch((error) => {
                        // eslint-выключение следующей строки
                        console.error(error);
                    })
            },
            onReset(evt) {
                evt.preventDefault()
                // Reset our form values
                this.form.title = ''
                this.form.description = ''

                this.form.coords = []
                this.show = false
                this.$nextTick(() => {
                    this.show = true
                })
            },
            onClick(e) {
                this.coords = e.get('coords');
                this.form.latitude = this.coords[0];
                this.form.longitude = this.coords[1];
            }
        }
    }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
