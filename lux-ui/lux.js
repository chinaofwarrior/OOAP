const LuxUI = (() => {
  const initDropdown = (dropdown) => {
    const trigger = dropdown.querySelector('[data-lux-dropdown-trigger]');
    const menu = dropdown.querySelector('[data-lux-dropdown-menu]');
    if (!trigger || !menu) return;
    const close = () => {
      dropdown.dataset.state = 'closed';
      trigger.setAttribute('aria-expanded', 'false');
      menu.hidden = true;
    };
    const open = () => {
      dropdown.dataset.state = 'open';
      trigger.setAttribute('aria-expanded', 'true');
      menu.hidden = false;
    };
    close();
    trigger.addEventListener('click', (event) => {
      event.stopPropagation();
      if (dropdown.dataset.state === 'open') {
        close();
      } else {
        open();
      }
    });
    document.addEventListener('click', (event) => {
      if (!dropdown.contains(event.target)) {
        close();
      }
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') close();
    });
  };

  const initTabs = (tabs) => {
    const triggers = Array.from(tabs.querySelectorAll('[data-lux-tab]'));
    const panels = Array.from(tabs.querySelectorAll('[data-lux-panel]'));
    if (triggers.length === 0 || panels.length === 0) return;
    const activate = (tabId) => {
      triggers.forEach((trigger) => {
        const active = trigger.dataset.luxTab === tabId;
        trigger.setAttribute('aria-selected', active ? 'true' : 'false');
        trigger.tabIndex = active ? 0 : -1;
      });
      panels.forEach((panel) => {
        const active = panel.dataset.luxPanel === tabId;
        panel.hidden = !active;
      });
    };
    triggers.forEach((trigger) => {
      trigger.addEventListener('click', () => activate(trigger.dataset.luxTab));
      trigger.addEventListener('keydown', (event) => {
        if (event.key !== 'ArrowRight' && event.key !== 'ArrowLeft') return;
        const currentIndex = triggers.indexOf(trigger);
        const nextIndex = event.key === 'ArrowRight'
          ? (currentIndex + 1) % triggers.length
          : (currentIndex - 1 + triggers.length) % triggers.length;
        triggers[nextIndex].focus();
        activate(triggers[nextIndex].dataset.luxTab);
      });
    });
    activate(triggers[0].dataset.luxTab);
  };

  const initModal = (modal) => {
    const closeButtons = Array.from(modal.querySelectorAll('[data-lux-close]'));
    const backdrop = document.querySelector(`[data-lux-backdrop="${modal.dataset.luxModal}"]`);
    const close = () => {
      modal.dataset.state = 'closed';
      modal.setAttribute('aria-hidden', 'true');
      if (backdrop) backdrop.dataset.state = 'closed';
    };
    closeButtons.forEach((button) => {
      button.addEventListener('click', close);
    });
    if (backdrop) {
      backdrop.addEventListener('click', close);
    }
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') close();
    });
    close();
  };

  const showToast = ({ title, description, variant = 'success', duration = 4000 }) => {
    let stack = document.querySelector('.lux-toast-stack');
    if (!stack) {
      stack = document.createElement('div');
      stack.className = 'lux-toast-stack';
      document.body.appendChild(stack);
    }
    const toast = document.createElement('div');
    toast.className = `lux-toast lux-toast--${variant}`;
    toast.setAttribute('role', 'status');
    const content = document.createElement('div');
    content.className = 'lux-stack';
    if (title) {
      const heading = document.createElement('div');
      heading.className = 'lux-text';
      heading.textContent = title;
      content.appendChild(heading);
    }
    if (description) {
      const text = document.createElement('div');
      text.className = 'lux-muted';
      text.textContent = description;
      content.appendChild(text);
    }
    toast.appendChild(content);
    stack.appendChild(toast);
    setTimeout(() => {
      toast.remove();
    }, duration);
  };

  const openModal = (id) => {
    const modal = document.querySelector(`[data-lux-modal="${id}"]`);
    const backdrop = document.querySelector(`[data-lux-backdrop="${id}"]`);
    if (!modal) return;
    modal.dataset.state = 'open';
    modal.setAttribute('aria-hidden', 'false');
    if (backdrop) backdrop.dataset.state = 'open';
  };

  const init = () => {
    document.querySelectorAll('[data-lux-dropdown]').forEach(initDropdown);
    document.querySelectorAll('[data-lux-tabs]').forEach(initTabs);
    document.querySelectorAll('[data-lux-modal]').forEach(initModal);
    document.querySelectorAll('[data-lux-open]').forEach((trigger) => {
      trigger.addEventListener('click', () => openModal(trigger.dataset.luxOpen));
    });
  };

  return { init, showToast, openModal };
})();

if (typeof window !== 'undefined') {
  window.LuxUI = LuxUI;
}
