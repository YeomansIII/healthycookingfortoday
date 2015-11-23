module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    // Task configuration goes here.

    concat: {
      app: {
        src: ['django-project/static/js/app/**/*.js'],
        dest: 'django-project/build/static/js/app.js'
      },
      vendor: {
        src: ['django-project/static/js/vendor/**/*.js'],
        dest: 'django-project/build/static/js/lib.js'
      }
    },

    uglify: {
      app: {
        files: {
          'django-project/build/static/js/app.min.js': ['django-project/static/js/app/**/*.js']
        }
      },
      vendor: {
        files: {
          'django-project/build/static/js/lib.min.js': ['django-project/static/js/vendor/**/*.js']
        }
      }
    },

    sass: {
      dev: {
        options: {
          sourceMap: true
        },
        files: {
          'django-project/build/static/css/main.css': 'django-project/static/scss/main.scss'
        }
      },
      deploy: {
        options: {
          sourceMap: true,
          outputStyle: 'compressed'
        },
        files: {
          'django-project/build/static/css/main.min.css': 'django-project/static/scss/main.scss'
        }
      }
    },

    imagemin: { // Task
      dynamic: { // Another target
        files: [{
          expand: true, // Enable dynamic expansion
          cwd: 'django-project/static/images/', // Src matches are relative to this path
          src: ['**/*.{png,jpg,gif}'], // Actual patterns to match
          dest: 'django-project/build/static/images/' // Destination path prefix
        }]
      }
    },

    watch: {
      options: {
        livereload: true
      },
      javascript: {
        files: ['django-project/static/js/app/**/*.js'],
        tasks: ['concat']
      },
      sass: {
        files: 'django-project/static/scss/**/*.scss',
        tasks: ['sass:dev']
      }
    }

  });

  // Load plugins here.
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-imagemin');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Register tasks here.
  grunt.registerTask('default', [
    'concat',
    'uglify',
    'sass',
    'imagemin',
    'watch'
  ]);

};
