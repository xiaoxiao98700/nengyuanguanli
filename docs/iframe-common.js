/**
 * Common helpers for pages rendered inside the main iframe containers.
 * Provides consistent tab-switching logic so each page does not have to
 * depend on parent window scripts.
 */
(function () {
    function setInitialTabVisibility(context) {
        const tabs = context.querySelectorAll('.tab-content');
        tabs.forEach(tab => {
            if (tab.classList.contains('active') || tab.getAttribute('data-active') === 'true' || tab.style.display === 'block') {
                tab.classList.add('active');
                tab.style.display = 'block';
            } else {
                tab.classList.remove('active');
                tab.style.display = 'none';
            }
        });
    }

    function createTabHandler() {
        return function handleTabSwitch(evt, tabId) {
            const origin = evt?.currentTarget;
            const container = origin?.closest('.sub-menu-content-container') || document;

            const tabs = container.querySelectorAll('.tab-content');
            tabs.forEach(tab => {
                const isTarget = tab.id === tabId;
                tab.classList.toggle('active', isTarget);
                tab.style.display = isTarget ? 'block' : 'none';
                if (isTarget && !tab.getAttribute('data-active')) {
                    tab.setAttribute('data-active', 'true');
                }
            });

            if (origin) {
                const buttons = origin.parentElement?.querySelectorAll('.tab-button') ||
                    container.querySelectorAll('.tab-button');
                buttons.forEach(btn => btn.classList.remove('active'));
                origin.classList.add('active');
            }
        };
    }

    const sharedTabHandler = createTabHandler();

    // Expose handler under the function names used by legacy markup
    window.openEnergyMonitorTab = sharedTabHandler;
    window.openEnergyTopologyTab = sharedTabHandler;

    document.addEventListener('DOMContentLoaded', () => {
        setInitialTabVisibility(document);
    });
})();

