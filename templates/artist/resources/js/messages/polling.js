$(function() {

	var polling = {
		lastTime : 0,
		messages : [],
		timer : null,
		idleCount : 0,
		interval : 60000
	}

	function doPoll() {
		$.ajax({
			url : path + '/notices/unre',
			type : 'get',
			data : {
				lastTime : polling.lastTime
			}
		}).then(function(data) {
			var messages = data.messages;
			var notices = data.notices;
			// 设置最后拉取时间
			polling.lastTime = messages.lastGetTime;
			if (messages.messageList.length > 0 || notices.length > 0) {
				// 有新信息，回调监听接口
				$('.navbar-red-dot').addClass('red-dot');
				if (messages.messageList.length > 0) {
					$('[data-notice=4]').find('span').addClass('red-dot');
				}
				if (notices.length > 0) {
					$.each(notices, function(i, v) {
						var url = '';
						var noticeId = 0;
						switch (v.type) {
						case 1:
							// 点赞
							noticeId = 1;
							url = path + '/notices/zanList';
							break;
						case 2:
							// 评论
							noticeId = 1;
							url = path + '/notices/commentList';
							break;
						case 3:
							// 回复
							noticeId = 1;
							url = path + '/notices/replyList';
							break;
						case 4:
							// 参加活动
							noticeId = 2;
							url = path + '/notices/eventList';
							break;
						case 5:
							// 获奖记录
							noticeId = 2;
							url = path + '/notices/awardList';
							break;
						case 6:
							// 约稿
							noticeId = 3;
							url = path + '/notices/projectList';
							break;
						}
						$('[data-notice=' + noticeId + ']').attr('href', url).find('span').addClass('red-dot');
					});
				}
				if (typeof (window.messagesNotice) === 'function')
					window.messagesNotice(data);
				if (typeof (window.onNewMessages) === 'function')
					window.onNewMessages(messages.messageList);
				// 空闲次数初始化为0
				polling.idleCount = 0;
				// 轮询间隔改为10秒
				polling.interval = 10000;
			} else {
				// 没有新消息
				// 空闲次数+1
				polling.idleCount++;
				// 轮询三次都没有新消息
				if (polling.idleCount > 2) {
					// 空闲次数初始化为0
					polling.idleCount = 0;
					// 轮询间隔*2
					polling.interval *= 2;
					// 轮询间隔到8分钟还没有新消息
					if (polling.interval >= 480000) {
						// 不再轮询了,等待刷新页面
						clearTimeout(polling.timer);
						polling.timer = null;
					}
				}
			}
		}).then(function() {
			polling.timer = setTimeout(doPoll, polling.interval)
		})
	}

	doPoll();
});