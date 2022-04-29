<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use App\Entity\Campaigns;
use App\Entity\BonusesUser;

class ProfileController extends AbstractController
{
    /**
     * @Route("/profile", name="profile")
     */
    public function index(): Response
    {
        $user = $this->getUser();

        if ($user) {
            $campaigns = $this->getDoctrine()->getRepository(Campaigns::class)->findBy(['user' => $user->getId()], ['id' => 'DESC']);
            $bonuses = $this->getDoctrine()->getRepository(BonusesUser::class)->findBy(['user' => $user->getId()], ['id' => 'DESC']);
            return $this->render('profile/index.html.twig', [
                'user' => $user,
                'campaigns' => $campaigns,
                'bonuses' => $bonuses,
            ]);
        } else {
            return $this->redirectToRoute('app_login');
        }
    }
}
