Задание 1
Настройте проект для работы с Celery. Также настройте приложение на работу с celery-beat для выполнения периодических задач.

Задание 2
Ранее вы реализовали функционал подписки на обновление курсов. Теперь добавьте асинхронную рассылку писем пользователям об обновлении материалов курса.

# redis установка в контейнер Docker
docker run --hostname=c12ae205511e --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --env=GOSU_VERSION=1.17 --env=REDIS_VERSION=7.4.1 --env=REDIS_DOWNLOAD_URL=http://download.redis.io/releases/redis-7.4.1.tar.gz --env=REDIS_DOWNLOAD_SHA=bc34b878eb89421bbfca6fa78752343bf37af312a09eb0fae47c9575977dfaa2 --volume=/data --network=bridge --workdir=/data -p 6379:6379 -p 8001:8001 --restart=no --runtime=runc -d redis:latest